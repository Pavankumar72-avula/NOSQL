import sys
from db import books_collection


# ------------------------------------------------------------------ #
#  BOOK DATA  –  160 books across 16 categories (one section each)
#  To add a book: put it in the right section.
#  To add a category: create a new section and register it in
#  BOOKS_BY_CATEGORY below.
# ------------------------------------------------------------------ #

# ==================== Fiction (10) ====================
FICTION_BOOKS = [
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780061120084-L.jpg"
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780451524935-L.jpg"
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780141439518-L.jpg"
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780743273565-L.jpg"
    },
    {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780060850524-L.jpg"
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J. D. Salinger",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780316769488-L.jpg"
    },
    {
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel García Márquez",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780060883287-L.jpg"
    },
    {
        "title": "The Kite Runner",
        "author": "Khaled Hosseini",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781594631931-L.jpg"
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780062315007-L.jpg"
    },
    {
        "title": "Animal Farm",
        "author": "George Orwell",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780451526342-L.jpg"
    },
]

# ==================== Science Fiction (10) ====================
SCIENCE_FICTION_BOOKS = [
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780441172719-L.jpg"
    },
    {
        "title": "Foundation",
        "author": "Isaac Asimov",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780553293357-L.jpg"
    },
    {
        "title": "Neuromancer",
        "author": "William Gibson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780441569595-L.jpg"
    },
    {
        "title": "Ender's Game",
        "author": "Orson Scott Card",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780812550702-L.jpg"
    },
    {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780345391803-L.jpg"
    },
    {
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781451673319-L.jpg"
    },
    {
        "title": "The Left Hand of Darkness",
        "author": "Ursula K. Le Guin",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780441478125-L.jpg"
    },
    {
        "title": "Snow Crash",
        "author": "Neal Stephenson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780553380958-L.jpg"
    },
    {
        "title": "The War of the Worlds",
        "author": "H. G. Wells",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780141441030-L.jpg"
    },
    {
        "title": "2001: A Space Odyssey",
        "author": "Arthur C. Clarke",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780451457998-L.jpg"
    },
]

# ==================== Fantasy (10) ====================
FANTASY_BOOKS = [
    {
        "title": "The Hobbit",
        "author": "J. R. R. Tolkien",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780547928227-L.jpg"
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J. K. Rowling",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780590353427-L.jpg"
    },
    {
        "title": "A Game of Thrones",
        "author": "George R. R. Martin",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780553593716-L.jpg"
    },
    {
        "title": "The Name of the Wind",
        "author": "Patrick Rothfuss",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780756404741-L.jpg"
    },
    {
        "title": "The Fellowship of the Ring",
        "author": "J. R. R. Tolkien",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780547928210-L.jpg"
    },
    {
        "title": "The Chronicles of Narnia",
        "author": "C. S. Lewis",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780064471190-L.jpg"
    },
    {
        "title": "Mistborn: The Final Empire",
        "author": "Brandon Sanderson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780765311788-L.jpg"
    },
    {
        "title": "The Way of Kings",
        "author": "Brandon Sanderson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780765326355-L.jpg"
    },
    {
        "title": "American Gods",
        "author": "Neil Gaiman",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780063081918-L.jpg"
    },
    {
        "title": "The Colour of Magic",
        "author": "Terry Pratchett",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780062225672-L.jpg"
    },
]

# ==================== Technology (10) ====================
TECHNOLOGY_BOOKS = [
    {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780132350884-L.jpg"
    },
    {
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780262033848-L.jpg"
    },
    {
        "title": "Design Patterns",
        "author": "Erich Gamma",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780201633610-L.jpg"
    },
    {
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780135957059-L.jpg"
    },
    {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781593279288-L.jpg"
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781593279929-L.jpg"
    },
    {
        "title": "Cracking the Coding Interview",
        "author": "Gayle Laakmann McDowell",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780984782857-L.jpg"
    },
    {
        "title": "Learning SQL",
        "author": "Alan Beaulieu",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781492057611-L.jpg"
    },
    {
        "title": "Head First Java",
        "author": "Kathy Sierra",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780596009205-L.jpg"
    },
    {
        "title": "Structure and Interpretation of Computer Programs",
        "author": "Harold Abelson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780262510875-L.jpg"
    },
    {
        "title": "Designing Data-Intensive Applications",
        "author": "Martin Kleppmann",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781449373320-L.jpg"
    },
    {
        "title": "Building Microservices",
        "author": "Sam Newman",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781492034025-L.jpg"
    },
    {
        "title": "Site Reliability Engineering",
        "author": "Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781491929124-L.jpg"
    },
    {
        "title": "Continuous Delivery",
        "author": "Jez Humble, David Farley",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780321601919-L.jpg"
    },
    {
        "title": "The Phoenix Project",
        "author": "Gene Kim, Kevin Behr, George Spafford",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780988262591-L.jpg"
    },
    {
        "title": "Compilers: Principles, Techniques, and Tools",
        "author": "Alfred V. Aho, Monica S. Lam, Ravi Sethi, Jeffrey D. Ullman",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780321486813-L.jpg"
    },
]

# ==================== Data Science (10) ====================
DATA_SCIENCE_BOOKS = [
    {
        "title": "Hands-On Machine Learning",
        "author": "Aurélien Géron",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781492032649-L.jpg"
    },
    {
        "title": "Python for Data Analysis",
        "author": "Wes McKinney",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781491957660-L.jpg"
    },
    {
        "title": "Deep Learning",
        "author": "Ian Goodfellow",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780262035613-L.jpg"
    },
    {
        "title": "The Elements of Statistical Learning",
        "author": "Trevor Hastie",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780387848570-L.jpg"
    },
    {
        "title": "Data Science from Scratch",
        "author": "Joel Grus",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781492041139-L.jpg"
    },
    {
        "title": "R for Data Science",
        "author": "Hadley Wickham",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781491910399-L.jpg"
    },
    {
        "title": "Pattern Recognition and Machine Learning",
        "author": "Christopher M. Bishop",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780387310732-L.jpg"
    },
    {
        "title": "Storytelling with Data",
        "author": "Cole Nussbaumer Knaflic",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781119002253-L.jpg"
    },
    {
        "title": "Naked Statistics",
        "author": "Charles Wheelan",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780393347777-L.jpg"
    },
    {
        "title": "An Introduction to Statistical Learning",
        "author": "Gareth James",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781461471370-L.jpg"
    },
]

# ==================== History (10) ====================
HISTORY_BOOKS = [
    {
        "title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780062316097-L.jpg"
    },
    {
        "title": "Guns, Germs, and Steel",
        "author": "Jared Diamond",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780393317558-L.jpg"
    },
    {
        "title": "A People's History of the United States",
        "author": "Howard Zinn",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780060838652-L.jpg"
    },
    {
        "title": "The Art of War",
        "author": "Sun Tzu",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781590302255-L.jpg"
    },
    {
        "title": "The Diary of a Young Girl",
        "author": "Anne Frank",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780553296983-L.jpg"
    },
    {
        "title": "Homo Deus: A Brief History of Tomorrow",
        "author": "Yuval Noah Harari",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780062464316-L.jpg"
    },
    {
        "title": "The History of the Ancient World",
        "author": "Susan Wise Bauer",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780393059748-L.jpg"
    },
    {
        "title": "A Short History of Nearly Everything",
        "author": "Bill Bryson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780767908184-L.jpg"
    },
    {
        "title": "The Rise and Fall of the Third Reich",
        "author": "William L. Shirer",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781451642599-L.jpg"
    },
    {
        "title": "1776",
        "author": "David McCullough",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780743226721-L.jpg"
    },
]

# ==================== Science (10) ====================
SCIENCE_BOOKS = [
    {
        "title": "A Brief History of Time",
        "author": "Stephen Hawking",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780553380163-L.jpg"
    },
    {
        "title": "The Origin of Species",
        "author": "Charles Darwin",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780451529060-L.jpg"
    },
    {
        "title": "Cosmos",
        "author": "Carl Sagan",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780345539434-L.jpg"
    },
    {
        "title": "The Selfish Gene",
        "author": "Richard Dawkins",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780199291151-L.jpg"
    },
    {
        "title": "Silent Spring",
        "author": "Rachel Carson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780618249060-L.jpg"
    },
    {
        "title": "The Gene: An Intimate History",
        "author": "Siddhartha Mukherjee",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781476733524-L.jpg"
    },
    {
        "title": "Astrophysics for People in a Hurry",
        "author": "Neil deGrasse Tyson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780393609394-L.jpg"
    },
    {
        "title": "The Elegant Universe",
        "author": "Brian Greene",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780393338102-L.jpg"
    },
    {
        "title": "Surely You're Joking, Mr. Feynman!",
        "author": "Richard P. Feynman",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780393316049-L.jpg"
    },
    {
        "title": "The Emperor of All Maladies",
        "author": "Siddhartha Mukherjee",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781439170915-L.jpg"
    },
]

# ==================== Philosophy (10) ====================
PHILOSOPHY_BOOKS = [
    {
        "title": "Meditations",
        "author": "Marcus Aurelius",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780140449334-L.jpg"
    },
    {
        "title": "The Republic",
        "author": "Plato",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780140455113-L.jpg"
    },
    {
        "title": "Beyond Good and Evil",
        "author": "Friedrich Nietzsche",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780140449235-L.jpg"
    },
    {
        "title": "The Prince",
        "author": "Niccolò Machiavelli",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780140449150-L.jpg"
    },
    {
        "title": "Thinking, Fast and Slow",
        "author": "Daniel Kahneman",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780374533557-L.jpg"
    },
    {
        "title": "Man's Search for Meaning",
        "author": "Viktor E. Frankl",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780807014295-L.jpg"
    },
    {
        "title": "The Nicomachean Ethics",
        "author": "Aristotle",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780140449495-L.jpg"
    },
    {
        "title": "Thus Spoke Zarathustra",
        "author": "Friedrich Nietzsche",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780140441185-L.jpg"
    },
    {
        "title": "The Art of Happiness",
        "author": "Dalai Lama",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781573227544-L.jpg"
    },
    {
        "title": "Sophie's World",
        "author": "Jostein Gaarder",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780374530716-L.jpg"
    },
]

# ==================== Biography (10) ====================
BIOGRAPHY_BOOKS = [
    {
        "title": "Steve Jobs",
        "author": "Walter Isaacson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781451648539-L.jpg"
    },
    {
        "title": "The Autobiography of Malcolm X",
        "author": "Malcolm X",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780345350688-L.jpg"
    },
    {
        "title": "Long Walk to Freedom",
        "author": "Nelson Mandela",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780316548182-L.jpg"
    },
    {
        "title": "Becoming",
        "author": "Michelle Obama",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781524763138-L.jpg"
    },
    {
        "title": "Einstein: His Life and Universe",
        "author": "Walter Isaacson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780743264747-L.jpg"
    },
    {
        "title": "The Diary of Frida Kahlo",
        "author": "Frida Kahlo",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780810959545-L.jpg"
    },
    {
        "title": "Wings of Fire",
        "author": "A. P. J. Abdul Kalam",
        "image_url": "https://covers.openlibrary.org/b/isbn/9788173711466-L.jpg"
    },
    {
        "title": "Elon Musk",
        "author": "Ashlee Vance",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780062301239-L.jpg"
    },
    {
        "title": "Leonardo da Vinci",
        "author": "Walter Isaacson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781501139154-L.jpg"
    },
    {
        "title": "I Know Why the Caged Bird Sings",
        "author": "Maya Angelou",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780345514400-L.jpg"
    },
]

# ==================== Self-Help (10) ====================
SELF_HELP_BOOKS = [
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780735211292-L.jpg"
    },
    {
        "title": "How to Win Friends and Influence People",
        "author": "Dale Carnegie",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780671027032-L.jpg"
    },
    {
        "title": "The 7 Habits of Highly Effective People",
        "author": "Stephen R. Covey",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781982137274-L.jpg"
    },
    {
        "title": "Rich Dad Poor Dad",
        "author": "Robert T. Kiyosaki",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781612680194-L.jpg"
    },
    {
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781577314806-L.jpg"
    },
    {
        "title": "The Subtle Art of Not Giving a F*ck",
        "author": "Mark Manson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780062457714-L.jpg"
    },
    {
        "title": "Mindset: The New Psychology of Success",
        "author": "Carol S. Dweck",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780345472328-L.jpg"
    },
    {
        "title": "Deep Work",
        "author": "Cal Newport",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781455586691-L.jpg"
    },
    {
        "title": "Think and Grow Rich",
        "author": "Napoleon Hill",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781585424337-L.jpg"
    },
    {
        "title": "The Four Agreements",
        "author": "Don Miguel Ruiz",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781878424310-L.jpg"
    },
]

# ==================== Mystery (10) ====================
MYSTERY_BOOKS = [
    {
        "title": "The Girl with the Dragon Tattoo",
        "author": "Stieg Larsson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780307454546-L.jpg"
    },
    {
        "title": "Gone Girl",
        "author": "Gillian Flynn",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780307588371-L.jpg"
    },
    {
        "title": "The Da Vinci Code",
        "author": "Dan Brown",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780307474278-L.jpg"
    },
    {
        "title": "Sherlock Holmes: The Complete Novels and Stories",
        "author": "Arthur Conan Doyle",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780553212419-L.jpg"
    },
    {
        "title": "And Then There Were None",
        "author": "Agatha Christie",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780062073488-L.jpg"
    },
    {
        "title": "The Silent Patient",
        "author": "Alex Michaelides",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781250301697-L.jpg"
    },
    {
        "title": "In the Woods",
        "author": "Tana French",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780143113492-L.jpg"
    },
    {
        "title": "The Woman in the Window",
        "author": "A. J. Finn",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780062678416-L.jpg"
    },
    {
        "title": "Big Little Lies",
        "author": "Liane Moriarty",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780399587191-L.jpg"
    },
    {
        "title": "Murder on the Orient Express",
        "author": "Agatha Christie",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780062693662-L.jpg"
    },
]

# ==================== Mathematics (10) ====================
MATHEMATICS_BOOKS = [
    {
        "title": "Gödel, Escher, Bach",
        "author": "Douglas R. Hofstadter",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780465026562-L.jpg"
    },
    {
        "title": "Calculus",
        "author": "James Stewart",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781285740621-L.jpg"
    },
    {
        "title": "Discrete Mathematics and Its Applications",
        "author": "Kenneth H. Rosen",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780073383095-L.jpg"
    },
    {
        "title": "Linear Algebra Done Right",
        "author": "Sheldon Axler",
        "image_url": "https://covers.openlibrary.org/b/isbn/9783319110790-L.jpg"
    },
    {
        "title": "The Art of Problem Solving Vol. 1",
        "author": "Sandor Lehoczky",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780977304561-L.jpg"
    },
    {
        "title": "How to Solve It",
        "author": "George Pólya",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780691164076-L.jpg"
    },
    {
        "title": "Concrete Mathematics",
        "author": "Ronald L. Graham",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780201558029-L.jpg"
    },
    {
        "title": "Probability and Statistics for Engineers",
        "author": "Ronald E. Walpole",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780321629111-L.jpg"
    },
    {
        "title": "Flatland: A Romance of Many Dimensions",
        "author": "Edwin A. Abbott",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780486272634-L.jpg"
    },
    {
        "title": "What Is Mathematics?",
        "author": "Richard Courant",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780195105193-L.jpg"
    },
]

# ==================== Business (10) ====================
BUSINESS_BOOKS = [
    {
        "title": "The Lean Startup",
        "author": "Eric Ries",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780307887894-L.jpg"
    },
    {
        "title": "Zero to One",
        "author": "Peter Thiel",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780804139298-L.jpg"
    },
    {
        "title": "Good to Great",
        "author": "Jim Collins",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780066620992-L.jpg"
    },
    {
        "title": "The Innovator's Dilemma",
        "author": "Clayton M. Christensen",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780062060242-L.jpg"
    },
    {
        "title": "Start with Why",
        "author": "Simon Sinek",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781591846444-L.jpg"
    },
    {
        "title": "Thinking in Bets",
        "author": "Annie Duke",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780735216358-L.jpg"
    },
    {
        "title": "The Hard Thing About Hard Things",
        "author": "Ben Horowitz",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780062273208-L.jpg"
    },
    {
        "title": "Principles",
        "author": "Ray Dalio",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781501124020-L.jpg"
    },
    {
        "title": "Shoe Dog",
        "author": "Phil Knight",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781501135910-L.jpg"
    },
    {
        "title": "The 4-Hour Workweek",
        "author": "Timothy Ferriss",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780307465351-L.jpg"
    },
]

# ==================== Psychology (10) ====================
PSYCHOLOGY_BOOKS = [
    {
        "title": "The Power of Habit",
        "author": "Charles Duhigg",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780812981605-L.jpg"
    },
    {
        "title": "Influence: The Psychology of Persuasion",
        "author": "Robert B. Cialdini",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780062937650-L.jpg"
    },
    {
        "title": "Emotional Intelligence",
        "author": "Daniel Goleman",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780553383713-L.jpg"
    },
    {
        "title": "Flow: The Psychology of Optimal Experience",
        "author": "Mihaly Csikszentmihalyi",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780061339202-L.jpg"
    },
    {
        "title": "Quiet: The Power of Introverts",
        "author": "Susan Cain",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780307352156-L.jpg"
    },
    {
        "title": "The Body Keeps the Score",
        "author": "Bessel van der Kolk",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780143127741-L.jpg"
    },
    {
        "title": "Predictably Irrational",
        "author": "Dan Ariely",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780061353246-L.jpg"
    },
    {
        "title": "Stumbling on Happiness",
        "author": "Daniel Gilbert",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781400077427-L.jpg"
    },
    {
        "title": "The Man Who Mistook His Wife for a Hat",
        "author": "Oliver Sacks",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780684853949-L.jpg"
    },
    {
        "title": "Outliers",
        "author": "Malcolm Gladwell",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780316017930-L.jpg"
    },
]

# ==================== Economics (10) ====================
ECONOMICS_BOOKS = [
    {
        "title": "Freakonomics",
        "author": "Steven D. Levitt",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780060731335-L.jpg"
    },
    {
        "title": "Capital in the Twenty-First Century",
        "author": "Thomas Piketty",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780674430006-L.jpg"
    },
    {
        "title": "The Wealth of Nations",
        "author": "Adam Smith",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780553585971-L.jpg"
    },
    {
        "title": "Thinking in Systems",
        "author": "Donella H. Meadows",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781603580557-L.jpg"
    },
    {
        "title": "Basic Economics",
        "author": "Thomas Sowell",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780465060733-L.jpg"
    },
    {
        "title": "Misbehaving",
        "author": "Richard H. Thaler",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780393352795-L.jpg"
    },
    {
        "title": "The Big Short",
        "author": "Michael Lewis",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780393338829-L.jpg"
    },
    {
        "title": "Doughnut Economics",
        "author": "Kate Raworth",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781603587969-L.jpg"
    },
    {
        "title": "Poor Economics",
        "author": "Abhijit V. Banerjee",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781610390934-L.jpg"
    },
    {
        "title": "Nudge",
        "author": "Richard H. Thaler",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780143115267-L.jpg"
    },
]

# ==================== Poetry (10) ====================
POETRY_BOOKS = [
    {
        "title": "The Complete Poems of Emily Dickinson",
        "author": "Emily Dickinson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780316184137-L.jpg"
    },
    {
        "title": "Leaves of Grass",
        "author": "Walt Whitman",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780486456768-L.jpg"
    },
    {
        "title": "The Waste Land and Other Poems",
        "author": "T. S. Eliot",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780451526847-L.jpg"
    },
    {
        "title": "Milk and Honey",
        "author": "Rupi Kaur",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781449474256-L.jpg"
    },
    {
        "title": "The Sun and Her Flowers",
        "author": "Rupi Kaur",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781449486792-L.jpg"
    },
    {
        "title": "The Prophet",
        "author": "Kahlil Gibran",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780394404288-L.jpg"
    },
    {
        "title": "Rumi: The Book of Love",
        "author": "Rumi",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780060750503-L.jpg"
    },
    {
        "title": "Selected Poems of Langston Hughes",
        "author": "Langston Hughes",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780679728184-L.jpg"
    },
    {
        "title": "Ariel",
        "author": "Sylvia Plath",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780060931728-L.jpg"
    },
    {
        "title": "Devotions",
        "author": "Mary Oliver",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780399563263-L.jpg"
    },
]



# ==================== Electronics & Electrical Engineering ====================
ELECTRONICS_BOOKS = [
    {
        "title": "The Art of Electronics",
        "author": "Paul Horowitz, Winfield Hill",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780521809269-L.jpg"
    },
    {
        "title": "Microelectronic Circuits",
        "author": "Adel S. Sedra, Kenneth C. Smith",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780199339136-L.jpg"
    },
    {
        "title": "Fundamentals of Electric Circuits",
        "author": "Charles K. Alexander, Matthew N. O. Sadiku",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780078028229-L.jpg"
    },
    {
        "title": "Digital Design: With an Introduction to the Verilog HDL",
        "author": "M. Morris Mano, Michael D. Ciletti",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780132774208-L.jpg"
    },
    {
        "title": "Signals and Systems",
        "author": "Alan V. Oppenheim, Alan S. Willsky",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780138147570-L.jpg"
    },
    {
        "title": "Electric Machinery Fundamentals",
        "author": "Stephen J. Chapman",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780073529547-L.jpg"
    },
    {
        "title": "Modern Control Engineering",
        "author": "Katsuhiko Ogata",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780136156734-L.jpg"
    },
    {
        "title": "CMOS VLSI Design: A Circuits and Systems Perspective",
        "author": "Neil H. E. Weste, David Harris",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780321547743-L.jpg"
    },
    {
        "title": "Electronic Devices and Circuit Theory",
        "author": "Robert L. Boylestad, Louis Nashelsky",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780132622264-L.jpg"
    },
    {
        "title": "Practical Electronics for Inventors",
        "author": "Paul Scherz, Simon Monk",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781259587542-L.jpg"
    },
    {
        "title": "Power System Analysis and Design",
        "author": "J. Duncan Glover, Mulukutla S. Sarma",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781305632134-L.jpg"
    },
    {
        "title": "Electromagnetic Waves and Radiating Systems",
        "author": "Edward C. Jordan, Keith G. Balmain",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780132499958-L.jpg"
    }
]

# ==================== Computer Engineering & Hardware ====================
COMPUTER_ENGINEERING_BOOKS = [
    {
        "title": "Computer Organization and Design: The Hardware/Software Interface",
        "author": "David A. Patterson, John L. Hennessy",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780128122754-L.jpg"
    },
    {
        "title": "Computer Architecture: A Quantitative Approach",
        "author": "John L. Hennessy, David A. Patterson",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780128119051-L.jpg"
    },
    {
        "title": "Code: The Hidden Language of Computer Hardware and Software",
        "author": "Charles Petzold",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780735611313-L.jpg"
    },
    {
        "title": "Modern Operating Systems",
        "author": "Andrew S. Tanenbaum, Herbert Bos",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780133591620-L.jpg"
    },
    {
        "title": "Computer Networking: A Top-Down Approach",
        "author": "James F. Kurose, Keith W. Ross",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780133594140-L.jpg"
    },
    {
        "title": "Operating System Concepts",
        "author": "Abraham Silberschatz, Peter B. Galvin",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781119800361-L.jpg"
    },
    {
        "title": "Database System Concepts",
        "author": "Abraham Silberschatz, Henry F. Korth",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780073523323-L.jpg"
    },
    {
        "title": "Embedded Systems: Real-Time Interfacing to ARM Cortex-M Microcontrollers",
        "author": "Jonathan W. Valvano",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781477508992-L.jpg"
    },
    {
        "title": "Computer Systems: A Programmer's Perspective",
        "author": "Randal E. Bryant, David R. O'Hallaron",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780134092669-L.jpg"
    },
    {
        "title": "The Hardware Hacker: Adventures in Making and Breaking Hardware",
        "author": "Andrew 'bunnie' Huang",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781593277581-L.jpg"
    }
]

# ==================== Mechanical Engineering ====================
MECHANICAL_ENGINEERING_BOOKS = [
    {
        "title": "Shigley's Mechanical Engineering Design",
        "author": "Richard G. Budynas, J. Keith Nisbett",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780073398204-L.jpg"
    },
    {
        "title": "Fundamentals of Fluid Mechanics",
        "author": "Bruce R. Munson, Donald F. Young",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781118116135-L.jpg"
    },
    {
        "title": "Fundamentals of Thermodynamics",
        "author": "Claus Borgnakke, Richard E. Sonntag",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781118131992-L.jpg"
    },
    {
        "title": "Mechanics of Materials",
        "author": "Ferdinand P. Beer, E. Russell Johnston Jr.",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780073398235-L.jpg"
    },
    {
        "title": "Vector Mechanics for Engineers: Statics and Dynamics",
        "author": "Ferdinand P. Beer, E. Russell Johnston Jr.",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780073398242-L.jpg"
    },
    {
        "title": "Heat and Mass Transfer: Fundamentals and Applications",
        "author": "Yunus A. Cengel, Afshin J. Ghajar",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780073398181-L.jpg"
    },
    {
        "title": "Theory of Machines and Mechanisms",
        "author": "John J. Uicker, Gordon R. Pennock",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780190264482-L.jpg"
    },
    {
        "title": "Introduction to Flight",
        "author": "John D. Anderson Jr.",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780078027673-L.jpg"
    },
    {
        "title": "Engineering Mechanics: Dynamics",
        "author": "J. L. Meriam, L. G. Kraige",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781118885840-L.jpg"
    },
    {
        "title": "Mechanical Vibrations",
        "author": "Singiresu S. Rao",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780134361307-L.jpg"
    }
]

# ==================== Civil & Structural Engineering ====================
CIVIL_ENGINEERING_BOOKS = [
    {
        "title": "Structural Analysis",
        "author": "Russell C. Hibbeler",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780134610672-L.jpg"
    },
    {
        "title": "Design of Concrete Structures",
        "author": "Arthur H. Nilson, David Darwin",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780073293493-L.jpg"
    },
    {
        "title": "Soil Mechanics and Foundations",
        "author": "Muni Budhu",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780470556849-L.jpg"
    },
    {
        "title": "Steel Design",
        "author": "William T. Segui",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781337094740-L.jpg"
    },
    {
        "title": "Surveying: Principles and Applications",
        "author": "Barry F. Kavanagh",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780137009404-L.jpg"
    },
    {
        "title": "Transportation Engineering: An Introduction",
        "author": "C. Jotin Khisty, B. Kent Lall",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780130335609-L.jpg"
    },
    {
        "title": "Water Resources Engineering",
        "author": "Larry W. Mays",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780470411995-L.jpg"
    },
    {
        "title": "Construction Planning, Equipment, and Methods",
        "author": "Robert L. Peurifoy, Clifford J. Schexnayder",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780072964202-L.jpg"
    }
]

# ==================== Robotics & Control Engineering ====================
ROBOTICS_BOOKS = [
    {
        "title": "Probabilistic Robotics",
        "author": "Sebastian Thrun, Wolfram Burgard, Dieter Fox",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780262201629-L.jpg"
    },
    {
        "title": "Modern Robotics: Mechanics, Planning, and Control",
        "author": "Kevin M. Lynch, Frank C. Park",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781107156302-L.jpg"
    },
    {
        "title": "Introduction to Autonomous Mobile Robots",
        "author": "Roland Siegwart, Illah R. Nourbakhsh",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780262015356-L.jpg"
    },
    {
        "title": "Robotics, Vision and Control: Fundamental Algorithms",
        "author": "Peter Corke",
        "image_url": "https://covers.openlibrary.org/b/isbn/9783319544137-L.jpg"
    },
    {
        "title": "Reinforcement Learning: An Introduction",
        "author": "Richard S. Sutton, Andrew G. Barto",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780262039246-L.jpg"
    },
    {
        "title": "Feedback Control of Dynamic Systems",
        "author": "Gene F. Franklin, J. David Powell",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780133496598-L.jpg"
    }
]

# ==================== Chemical & Materials Engineering ====================
CHEMICAL_MATERIALS_BOOKS = [
    {
        "title": "Elements of Chemical Reaction Engineering",
        "author": "H. Scott Fogler",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780133887518-L.jpg"
    },
    {
        "title": "Materials Science and Engineering: An Introduction",
        "author": "William D. Callister Jr., David G. Rethwisch",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781119405498-L.jpg"
    },
    {
        "title": "Perry's Chemical Engineers' Handbook",
        "author": "Don W. Green, Robert H. Perry",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780071422949-L.jpg"
    },
    {
        "title": "Unit Operations of Chemical Engineering",
        "author": "Warren L. McCabe, Julian C. Smith",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780072848236-L.jpg"
    },
    {
        "title": "Chemical Engineering Thermodynamics",
        "author": "J. M. Smith, H. C. Van Ness",
        "image_url": "https://covers.openlibrary.org/b/isbn/9781259696527-L.jpg"
    },
    {
        "title": "Introduction to Materials Management",
        "author": "J. R. Tony Arnold, Stephen N. Chapman",
        "image_url": "https://covers.openlibrary.org/b/isbn/9780132371926-L.jpg"
    }
]


# ------------------------------------------------------------------ #
#  NEW ENGINEERING & CS CATEGORIES
# ------------------------------------------------------------------ #

COMPUTER_SCIENCE_BOOKS = [
    {"title": "Data Structures and Algorithms in Python", "author": "Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser", "image_url": "https://covers.openlibrary.org/b/isbn/9781118290279-L.jpg"},
    {"title": "The Algorithm Design Manual", "author": "Steven S. Skiena", "image_url": "https://covers.openlibrary.org/b/isbn/9781848000698-L.jpg"},
    {"title": "Fundamentals of Database Systems", "author": "Ramez Elmasri, Shamkant B. Navathe", "image_url": "https://covers.openlibrary.org/b/isbn/9780133970777-L.jpg"},
    {"title": "Computer Networks", "author": "Andrew S. Tanenbaum, David J. Wetherall", "image_url": "https://covers.openlibrary.org/b/isbn/9780132126953-L.jpg"},
    {"title": "Operating Systems: Three Easy Pieces", "author": "Remzi H. Arpaci-Dusseau, Andrea C. Arpaci-Dusseau", "image_url": "https://covers.openlibrary.org/b/isbn/9781985086593-L.jpg"},
    {"title": "The C Programming Language", "author": "Brian W. Kernighan, Dennis M. Ritchie", "image_url": "https://covers.openlibrary.org/b/isbn/9780131103627-L.jpg"},
    {"title": "Programming Pearls", "author": "Jon Bentley", "image_url": "https://covers.openlibrary.org/b/isbn/9780201657883-L.jpg"},
    {"title": "Software Engineering: A Practitioner's Approach", "author": "Roger S. Pressman, Bruce Maxim", "image_url": "https://covers.openlibrary.org/b/isbn/9780078022128-L.jpg"},
]

AI_ML_BOOKS = [
    {"title": "Artificial Intelligence: A Modern Approach", "author": "Stuart J. Russell, Peter Norvig", "image_url": "https://covers.openlibrary.org/b/isbn/9780134610993-L.jpg"},
    {"title": "Machine Learning", "author": "Tom M. Mitchell", "image_url": "https://covers.openlibrary.org/b/isbn/9780070428072-L.jpg"},
    {"title": "Neural Networks and Deep Learning", "author": "Michael A. Nielsen", "image_url": "https://covers.openlibrary.org/b/isbn/9780983-L.jpg"},
    {"title": "Speech and Language Processing", "author": "Daniel Jurafsky, James H. Martin", "image_url": "https://covers.openlibrary.org/b/isbn/9780131873216-L.jpg"},
    {"title": "Natural Language Processing with Python", "author": "Steven Bird, Ewan Klein, Edward Loper", "image_url": "https://covers.openlibrary.org/b/isbn/9780596516499-L.jpg"},
    {"title": "Probabilistic Graphical Models", "author": "Daphne Koller, Nir Friedman", "image_url": "https://covers.openlibrary.org/b/isbn/9780262013192-L.jpg"},
    {"title": "Computer Vision: Algorithms and Applications", "author": "Richard Szeliski", "image_url": "https://covers.openlibrary.org/b/isbn/9781848829343-L.jpg"},
    {"title": "Mining of Massive Datasets", "author": "Jure Leskovec, Anand Rajaraman, Jeffrey D. Ullman", "image_url": "https://covers.openlibrary.org/b/isbn/9781107077232-L.jpg"},
]

ECE_BOOKS = [
    {"title": "Communication Systems", "author": "Simon Haykin", "image_url": "https://covers.openlibrary.org/b/isbn/9780471178699-L.jpg"},
    {"title": "Digital Communications", "author": "John G. Proakis, Masoud Salehi", "image_url": "https://covers.openlibrary.org/b/isbn/9780072957167-L.jpg"},
    {"title": "Modern Digital and Analog Communication Systems", "author": "B. P. Lathi, Zhi Ding", "image_url": "https://covers.openlibrary.org/b/isbn/9780195384932-L.jpg"},
    {"title": "Wireless Communications: Principles and Practice", "author": "Theodore S. Rappaport", "image_url": "https://covers.openlibrary.org/b/isbn/9780130422323-L.jpg"},
    {"title": "Antenna Theory: Analysis and Design", "author": "Constantine A. Balanis", "image_url": "https://covers.openlibrary.org/b/isbn/9780470588727-L.jpg"},
    {"title": "Digital Signal Processing: Principles, Algorithms and Applications", "author": "John G. Proakis, Dimitris G. Manolakis", "image_url": "https://covers.openlibrary.org/b/isbn/9780131873742-L.jpg"},
]

ENGINEERING_MATH_BOOKS = [
    {"title": "Advanced Engineering Mathematics", "author": "Erwin Kreyszig", "image_url": "https://covers.openlibrary.org/b/isbn/9780470458365-L.jpg"},
    {"title": "Engineering Mathematics", "author": "K. A. Stroud, Dexter J. Booth", "image_url": "https://covers.openlibrary.org/b/isbn/9780831134709-L.jpg"},
    {"title": "Advanced Engineering Mathematics", "author": "Dennis G. Zill", "image_url": "https://covers.openlibrary.org/b/isbn/9781284105902-L.jpg"},
    {"title": "Numerical Methods for Engineers", "author": "Steven C. Chapra, Raymond P. Canale", "image_url": "https://covers.openlibrary.org/b/isbn/9780073397924-L.jpg"},
    {"title": "Mathematical Methods for Physicists", "author": "George B. Arfken, Hans J. Weber", "image_url": "https://covers.openlibrary.org/b/isbn/9780120598762-L.jpg"},
    {"title": "Ordinary Differential Equations", "author": "Morris Tenenbaum, Harry Pollard", "image_url": "https://covers.openlibrary.org/b/isbn/9780486649405-L.jpg"},
]
# ------------------------------------------------------------------ #
#  CATEGORY REGISTRY
# ------------------------------------------------------------------ #

BOOKS_BY_CATEGORY = {
    "Technology": TECHNOLOGY_BOOKS,
    "Electronics & Electrical Engineering": ELECTRONICS_BOOKS,
    "Computer Engineering": COMPUTER_ENGINEERING_BOOKS,
    "Mechanical Engineering": MECHANICAL_ENGINEERING_BOOKS,
    "Civil & Structural Engineering": CIVIL_ENGINEERING_BOOKS,
    "Robotics & Control Engineering": ROBOTICS_BOOKS,
    "Chemical & Materials Engineering": CHEMICAL_MATERIALS_BOOKS,
    "Data Science": DATA_SCIENCE_BOOKS,
    "Science": SCIENCE_BOOKS,
    "Mathematics": MATHEMATICS_BOOKS,
    "Science Fiction": SCIENCE_FICTION_BOOKS,
    "Fiction": FICTION_BOOKS,
    "Fantasy": FANTASY_BOOKS,
    "History": HISTORY_BOOKS,
    "Philosophy": PHILOSOPHY_BOOKS,
    "Biography": BIOGRAPHY_BOOKS,
    "Self-Help": SELF_HELP_BOOKS,
    "Mystery": MYSTERY_BOOKS,
    "Business": BUSINESS_BOOKS,
    "Psychology": PSYCHOLOGY_BOOKS,
    "Economics": ECONOMICS_BOOKS,
    "Poetry": POETRY_BOOKS,
    "Computer Science and Engineering": COMPUTER_SCIENCE_BOOKS,
    "Artificial Intelligence and Machine Learning": AI_ML_BOOKS,
    "Electronics and Communication Engineering": ECE_BOOKS,
    "Engineering Mathematics": ENGINEERING_MATH_BOOKS,
}


# Flat list used by seed_books(): each book gets its "category" field added
SEED_BOOKS = [
    {**book, "category": category}
    for category, books in BOOKS_BY_CATEGORY.items()
    for book in books
]


# ------------------------------------------------------------------ #
#  SEED LOGIC
# ------------------------------------------------------------------ #

def seed_books():
    """Insert books into MongoDB, skipping duplicates by title."""

    inserted = 0
    skipped  = 0

    # Fetch all existing titles once (case-insensitive comparison)
    existing_titles = {
        book["title"].lower()
        for book in books_collection.find({}, {"title": 1})
    }

    new_books = []

    for book in SEED_BOOKS:
        if book["title"].lower() in existing_titles:
            skipped += 1
        else:
            new_books.append(book)

    if new_books:
        result = books_collection.insert_many(new_books)
        inserted = len(result.inserted_ids)

    print("\n" + "=" * 50)
    print("          BOOK SEEDING RESULTS")
    print("=" * 50)
    print(f"  Total books in seed data : {len(SEED_BOOKS)}")
    print(f"  Already existed (skipped): {skipped}")
    print(f"  Newly inserted           : {inserted}")
    print(f"  Total books in collection: {books_collection.count_documents({})}")
    print("=" * 50 + "\n")

    return inserted


# ------------------------------------------------------------------ #
#  MAIN
# ------------------------------------------------------------------ #

if __name__ == "__main__":

    skip_sync = "--skip-sync" in sys.argv

    try:
        count = seed_books()

        if count > 0 and not skip_sync:

            print("Syncing new books to Neo4j...")

            from sync_books import sync_books
            sync_books()

            print("Neo4j sync completed!\n")

        elif skip_sync:
            print("Neo4j sync skipped (--skip-sync flag).\n")

        else:
            print("No new books to sync.\n")

    except Exception as e:
        print(f"Seeding failed: {e}")
        raise