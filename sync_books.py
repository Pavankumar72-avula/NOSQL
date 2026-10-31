
from db import books_collection, users_collection, loans_collection
from neo4j_db import driver, NEO4J_DATABASE


def sync_books():

    # Get data from MongoDB
    books = list(books_collection.find())
    users = list(users_collection.find())
    loans = list(loans_collection.find())

    synced_books = 0
    synced_students = 0
    synced_loans = 0

    with driver.session(database=NEO4J_DATABASE) as session:

        # ---------------- CREATE CONSTRAINTS ----------------

        session.run("""
            CREATE CONSTRAINT book_mongo_id IF NOT EXISTS
            FOR (b:Book)
            REQUIRE b.mongo_id IS UNIQUE
        """).consume()

        session.run("""
            CREATE CONSTRAINT category_name IF NOT EXISTS
            FOR (c:Category)
            REQUIRE c.name IS UNIQUE
        """).consume()

        session.run("""
            CREATE CONSTRAINT student_mongo_id IF NOT EXISTS
            FOR (s:Student)
            REQUIRE s.mongo_id IS UNIQUE
        """).consume()

        # ---------------- SYNC BOOKS ----------------

        for book in books:

            mongo_id = str(book["_id"])

            title = book.get("title", "Untitled")
            author = book.get("author", "Unknown")
            category = book.get("category", "Uncategorized")
            image_url = book.get("image_url", "")

            # Create or update book
            session.run("""
                MERGE (b:Book {mongo_id: $mongo_id})

                SET
                    b.title = $title,
                    b.author = $author,
                    b.category = $category,
                    b.image_url = $image_url

                MERGE (c:Category {name: $category})

                MERGE (b)-[:BELONGS_TO]->(c)
            """,
                mongo_id=mongo_id,
                title=title,
                author=author,
                category=category,
                image_url=image_url
            ).consume()

            synced_books += 1

        # ---------------- SYNC STUDENTS ----------------

        for user in users:

            # Only student accounts
            if user.get("role") != "student":
                continue

            student_id = str(user["_id"])

            name = user.get("name", "Unknown")
            email = user.get("email", "")

            session.run("""
                MERGE (s:Student {mongo_id: $student_id})

                SET
                    s.name = $name,
                    s.email = $email
            """,
                student_id=student_id,
                name=name,
                email=email
            ).consume()

            synced_students += 1

        # ---------------- SYNC ACTIVE LOANS ----------------

        # Remove old active borrowing relationships
        session.run("""
            MATCH ()-[r:BORROWED]->()
            DELETE r
        """).consume()

        for loan in loans:

            # Only currently borrowed books
            if loan.get("status") != "borrowed":
                continue

            student_id = str(loan.get("user_id", ""))
            book_id = str(loan.get("book_id", ""))

            borrowed_at = loan.get("borrowed_at")
            due_date = loan.get("due_date")

            # Create borrowing relationship
            session.run("""
                MATCH (s:Student {mongo_id: $student_id})
                MATCH (b:Book {mongo_id: $book_id})

                MERGE (s)-[r:BORROWED]->(b)

                SET
                    r.borrowed_at = $borrowed_at,
                    r.due_date = $due_date,
                    r.status = 'borrowed'
            """,
                student_id=student_id,
                book_id=book_id,
                borrowed_at=borrowed_at,
                due_date=due_date
            ).consume()

            synced_loans += 1

    # ---------------- SYNC RESULTS ----------------

    print("\n========== SYNCHRONIZATION RESULTS ==========")

    print(f"MongoDB books found: {len(books)}")
    print(f"Books synchronized: {synced_books}")

    print(f"MongoDB users found: {len(users)}")
    print(f"Students synchronized: {synced_students}")

    print(f"Active loans synchronized: {synced_loans}")

    print("==========================================\n")


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":

    try:

        sync_books()

        print(
            "MongoDB to Neo4j synchronization completed successfully!"
        )

    except Exception:

        print("Synchronization failed.")

        raise

    finally:

        driver.close()
