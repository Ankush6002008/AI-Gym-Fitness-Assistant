import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Load environment variables
load_dotenv()

# Read MongoDB URI
MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI not found in .env")

# Create MongoDB client
client = MongoClient(MONGODB_URI)

# Database name
db = client["ai_gym_assistant"]


def test_connection():
    try:
        client.admin.command("ping")
        print("✅ MongoDB Connected Successfully")
    except ConnectionFailure:
        print("❌ Failed to connect to MongoDB")