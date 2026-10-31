
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is missing from .env")


client = MongoClient(
    MONGODB_URI,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=30000,
    connectTimeoutMS=30000,
    socketTimeoutMS=30000
)

db = client["library_management"]

books_collection = db["books"]
users_collection = db["users"]
loans_collection = db["loans"]
db = client["library"]
