
import os
from datetime import datetime, timedelta, timezone
from db import db, books_collection, users_collection
from neo4j_db import driver, NEO4J_DATABASE

from collections import defaultdict


from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)
from bson import ObjectId
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

# Load environment variables before initializing the app
load_dotenv()

from db import db, books_collection, users_collection
from auth import login_required, admin_required


app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

if not app.secret_key:
    raise RuntimeError("FLASK_SECRET_KEY is missing from .env")

loans_collection = db["loans"]


# ---------------- HOME / BOOK CATALOGUE ----------------



@app.route("/")
def home():
    search = request.args.get("search", "").strip()
    selected_category = request.args.get("category", "").strip()

    query = {}

    # Search by title, author, or category
    if search:
        query = {
            "$or": [
                {"title": {"$regex": search, "$options": "i"}},
                {"author": {"$regex": search, "$options": "i"}},
                {"category": {"$regex": search, "$options": "i"}}
            ]
        }

    # Filter by selected category
    if selected_category:
        if "$or" in query:
            query = {
                "$and": [
                    query,
                    {"category": selected_category}
                ]
            }
        else:
            query = {"category": selected_category}

    # Fetch books from MongoDB
    books = list(
        books_collection.find(query).sort([
            ("category", 1),
            ("title", 1)
        ])
    )

    # Convert MongoDB ObjectId to string
    for book in books:
        book["_id"] = str(book["_id"])

    # Group books category-wise
    books_by_category = {}

    for book in books:
        category = book.get("category") or "Uncategorized"

        books_by_category.setdefault(
            category, []
        ).append(book)

    # Sort categories alphabetically
    books_by_category = dict(
        sorted(books_by_category.items())
    )

    # Get all available categories
    all_categories = sorted(
        category
        for category in books_collection.distinct("category")
        if category
    )

    # Library-wide stats for the hero section
    total_books  = books_collection.count_documents({})
    total_users  = users_collection.count_documents({})
    active_loans = loans_collection.count_documents({"status": "borrowed"})

    return render_template(
        "index.html",
        books=books,
        books_by_category=books_by_category,
        all_categories=all_categories,
        selected_category=selected_category,
        search=search,
        total_books=total_books,
        total_users=total_users,
        active_loans=active_loans,
    )




# ---------------- ADD BOOK (ADMIN) ----------------

@app.route("/add-book", methods=["POST"])
@admin_required
def add_book():
    title = request.form.get("title", "").strip()
    author = request.form.get("author", "").strip()
    category = request.form.get("category", "").strip()
    image_url = request.form.get("image_url", "").strip()

    if not all([title, author, category]):
        flash("Please fill in all required fields.")
        return redirect(url_for("home"))

    try:
        books_collection.insert_one({
            "title": title,
            "author": author,
            "category": category,
            "image_url": image_url
        })

        flash("Book added successfully!")

    except Exception:
        app.logger.exception("Failed to add book.")
        flash("Could not add the book. Please try again.")

    return redirect(url_for("home"))


# ---------------- EDIT BOOK (ADMIN) ----------------

@app.route("/edit-book/<book_id>", methods=["GET", "POST"])
@admin_required
def edit_book(book_id):
    if not ObjectId.is_valid(book_id):
        flash("Invalid book ID.")
        return redirect(url_for("home"))

    book = books_collection.find_one({
        "_id": ObjectId(book_id)
    })

    if book is None:
        flash("Book not found.")
        return redirect(url_for("home"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        category = request.form.get("category", "").strip()
        

        if not all([title, author, category]):
            flash("Please fill in all fields.")
            return redirect(
                url_for("edit_book", book_id=book_id)
            )

        books_collection.update_one(
            {"_id": ObjectId(book_id)},
            {"$set": {
                "title": title,
                "author": author,
                "category": category,
                "image_url": request.form.get("image_url", "").strip()
            }}
        )

        flash("Book updated successfully!")
        return redirect(url_for("home"))

    return render_template("edit_book.html", book=book)


# ---------------- DELETE BOOK (ADMIN) ----------------

@app.route("/delete-book/<book_id>", methods=["POST"])
@admin_required
def delete_book(book_id):
    if not ObjectId.is_valid(book_id):
        flash("Invalid book ID.")
        return redirect(url_for("home"))

    # Don't delete a book while it has an active loan
    active_loan = loans_collection.find_one({
        "book_id": book_id,
        "status": "borrowed"
    })

    if active_loan:
        flash("This book is currently borrowed and cannot be deleted.")
        return redirect(url_for("home"))

    result = books_collection.delete_one({
        "_id": ObjectId(book_id)
    })

    if result.deleted_count:
        flash("Book deleted successfully!")
    else:
        flash("Book not found.")

    return redirect(url_for("home"))


# ---------------- BORROW BOOK (STUDENT) ----------------


# ---------------- BORROW BOOK ----------------

@app.route("/borrow/<book_id>", methods=["POST"])
@login_required
def borrow_book(book_id):

    # 1. Only students can borrow books
    if session.get("role") != "student":
        flash("Only student accounts can borrow books.")
        return redirect(url_for("home"))

    # 2. Validate the book ID
    if not ObjectId.is_valid(book_id):
        flash("Invalid book ID.")
        return redirect(url_for("home"))

    try:
        # 3. Find the selected book
        book = books_collection.find_one({
            "_id": ObjectId(book_id)
        })

        if book is None:
            flash("Book not found.")
            return redirect(url_for("home"))

        user_id = session.get("user_id")
        loans_collection = db["loans"]

        # 4. Prevent duplicate active loans
        existing_loan = loans_collection.find_one({
            "user_id": user_id,
            "book_id": book_id,
            "status": "borrowed"
        })

        if existing_loan:
            flash("You have already borrowed this book.")
            return redirect(url_for("dashboard"))

        # 5. Create the borrowing record
        borrowed_at = datetime.now(timezone.utc)
        due_date = borrowed_at + timedelta(days=14)

        loan = {
            "user_id": user_id,
            "book_id": book_id,
            "book_title": book.get("title", "Untitled"),
            "borrowed_at": borrowed_at,
            "due_date": due_date,
            "returned_at": None,
            "status": "borrowed"
        }

        # 6. Save the record in MongoDB
        result = loans_collection.insert_one(loan)

        if result.inserted_id:
            flash("Book borrowed successfully!")
            return redirect(url_for("dashboard"))

        flash("Borrowing failed. Please try again.")
        return redirect(url_for("home"))

    except Exception:
        app.logger.exception("Error while borrowing book.")
        flash("An error occurred while borrowing the book.")
        return redirect(url_for("home"))

  
# ---------------- RETURN BOOK ----------------

@app.route("/return/<loan_id>", methods=["POST"])
@login_required
def return_book(loan_id):

    # Only students can return books
    if session.get("role") != "student":
        flash("Only student accounts can return books.")
        return redirect(url_for("dashboard"))

    # Validate the loan ID
    if not ObjectId.is_valid(loan_id):
        flash("Invalid loan ID.")
        return redirect(url_for("dashboard"))

    try:
        user_id = session.get("user_id")
        loans_collection = db["loans"]

        # Find an active loan belonging to this student
        loan = loans_collection.find_one({
            "_id": ObjectId(loan_id),
            "user_id": user_id,
            "status": "borrowed"
        })

        if loan is None:
            flash("Active borrowing record not found.")
            return redirect(url_for("dashboard"))

        # Update the existing loan instead of deleting it
        result = loans_collection.update_one(
            {
                "_id": ObjectId(loan_id),
                "user_id": user_id,
                "status": "borrowed"
            },
            {
                "$set": {
                    "status": "returned",
                    "returned_at": datetime.now(timezone.utc)
                }
            }
        )

        if result.modified_count == 1:
            flash("Book returned successfully!")
        else:
            flash("The book could not be returned. Please try again.")

        return redirect(url_for("dashboard"))

    except Exception:
        app.logger.exception("Error while returning book.")
        flash("An error occurred while returning the book.")
        return redirect(url_for("dashboard"))



# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm_password", "")

        if not name or not email or not password:
            flash("Please fill in all required fields.")
            return redirect(url_for("register"))

        # Minimum password length
        if len(password) < 8:
            flash("Password must contain at least 8 characters.")
            return redirect(url_for("register"))

        # Confirm password
        if password != confirm:
            flash("Passwords do not match.")
            return redirect(url_for("register"))

        # Check existing email
        if users_collection.find_one({"email": email}):
            flash("An account with this email already exists.")
            return redirect(url_for("register"))

        # Create student account
        users_collection.insert_one({
            "name": name,
            "email": email,
            "password_hash": generate_password_hash(password),
            "role": "student"
        })

        flash("Registration successful. Please log in.")
        return redirect(url_for("login"))

    return render_template("register.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = users_collection.find_one({"email": email})

        if not user or not check_password_hash(
            user.get("password_hash", ""), password
        ):
            flash("Invalid email or password.")
            return redirect(url_for("login"))

        session.clear()
        session["user_id"] = str(user["_id"])
        session["name"] = user["name"]
        session["role"] = user["role"]

        flash("Login successful!")
        return redirect(url_for("home"))

    return render_template("login.html")


# ---------------- LOGOUT ----------------

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    session.clear()
    flash("You have logged out.")
    return redirect(url_for("login"))



# ---------------- BOOK RECOMMENDATIONS ----------------

def get_recommendations(user_id):

    query = """
    MATCH (student:Student {mongo_id: $user_id})
          -[:BORROWED]->(borrowed:Book)
          -[:BELONGS_TO]->(category:Category)

    MATCH (recommended:Book)-[:BELONGS_TO]->(category)

    WHERE NOT EXISTS {
        MATCH (student)-[:BORROWED]->(alreadyBorrowed:Book)
        WHERE alreadyBorrowed.mongo_id = recommended.mongo_id
    }

    RETURN DISTINCT
        recommended.mongo_id AS book_id,
        recommended.title AS title,
        recommended.author AS author,
        category.name AS category,
        recommended.image_url AS image_url

    LIMIT 10
    """

    try:
        with driver.session(database=NEO4J_DATABASE) as neo_session:

            result = neo_session.run(
                query,
                user_id=user_id
            )

            recommendations = [
                record.data()
                for record in result
            ]

            return recommendations

    except Exception:
        app.logger.exception(
            "Failed to fetch book recommendations."
        )

        return []






# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
@login_required
def dashboard():

    user_id = session.get("user_id")

    try:

        borrowed_books = list(
            loans_collection.find({
                "user_id": user_id,
                "status": "borrowed"
            }).sort("borrowed_at", -1)
        )

        # Attach book information to each loan
        for loan in borrowed_books:

            book_id = str(loan.get("book_id", ""))

            book = None

            if ObjectId.is_valid(book_id):

                book = books_collection.find_one({
                    "_id": ObjectId(book_id)
                })

            if book:

                loan["title"] = book.get(
                    "title", "Unknown Book"
                )

                loan["author"] = book.get(
                    "author", "Unknown"
                )

                loan["image_url"] = book.get(
                    "image_url", ""
                )

            else:

                loan["title"] = "Book Not Found"
                loan["author"] = "Unknown"
                loan["image_url"] = ""

        recommendations = get_recommendations(user_id)

        return render_template(
            "dashboard.html",
            borrowed_books=borrowed_books,
            recommendations=recommendations
        )

    except Exception:

        app.logger.exception(
            "Failed to load dashboard."
        )

        flash("Could not load your dashboard.")

        return render_template(
            "dashboard.html",
            borrowed_books=[],
            recommendations=[]
        )



# ---------------- ADMIN DASHBOARD ----------------

@app.route("/admin")
@admin_required
def admin_dashboard():
    try:
        total_books    = books_collection.count_documents({})
        total_users    = users_collection.count_documents({})
        active_loans   = loans_collection.count_documents({"status": "borrowed"})
        returned_loans = loans_collection.count_documents({"status": "returned"})
        available_books = total_books - active_loans

        all_loans = list(
            loans_collection.find().sort("borrowed_at", -1).limit(100)
        )
        for loan in all_loans:
            loan["_id"] = str(loan["_id"])

        all_users = list(users_collection.find({}, {
            "_id": 1, "name": 1, "email": 1, "role": 1
        }))
        for u in all_users:
            u["_id"] = str(u["_id"])
            u["active_loans"] = loans_collection.count_documents({
                "user_id": str(u["_id"]),
                "status": "borrowed"
            })

        all_categories = sorted(
            cat for cat in books_collection.distinct("category") if cat
        )
        category_counts = {
            cat: books_collection.count_documents({"category": cat})
            for cat in all_categories
        }

        return render_template(
            "admin.html",
            total_books=total_books,
            total_users=total_users,
            active_loans=active_loans,
            returned_loans=returned_loans,
            available_books=available_books,
            all_loans=all_loans,
            all_users=all_users,
            category_counts=category_counts,
        )

    except Exception:
        app.logger.exception("Failed to load admin dashboard.")
        flash("Could not load the admin dashboard.")
        return redirect(url_for("home"))


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":
    app.run(debug=True)
