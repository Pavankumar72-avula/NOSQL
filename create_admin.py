import os
from getpass import getpass
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from pymongo import MongoClient

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
users = client["library_management"]["users"]

try:
    client.admin.command("ping")

    email = input("Admin email: ").strip().lower()
    name = input("Admin name: ").strip()
    password = getpass("Admin password (minimum 12 characters): ")

    if not email or not name or len(password) < 12:
        raise ValueError(
            "Email and name are required; password must have 12+ characters."
        )

    if users.find_one({"email": email}):
        raise ValueError("An account with this email already exists.")

    users.insert_one({
        "name": name,
        "email": email,
        "password_hash": generate_password_hash(password),
        "role": "admin"
    })

    print("Administrator account created successfully.")

finally:
    client.close()