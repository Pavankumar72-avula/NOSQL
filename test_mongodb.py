import os
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient

from db import MONGODB_URI
client = MongoClient(
    MONGODB_URI,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=15000
)

load_dotenv()

uri = os.getenv("MONGODB_URI")

if not uri:
    raise ValueError("MONGODB_URI not found. Check your .env file.")

client = MongoClient(uri, serverSelectionTimeoutMS=10000)

try:
    client.admin.command("ping")
    print("MongoDB Atlas connected successfully!")

    db = client["library_management"]

    db.books.insert_one({
        "title": "Python Programming",
        "category": "Technology"
    })

    print("Test book inserted successfully!")

except Exception as error:
    print("Connection error:", error)

finally:
    client.close()