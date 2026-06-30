import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# Get MongoDB URI from .env
MONGODB_URI = os.getenv("MONGODB_URI")

# Create MongoDB client
client = MongoClient(MONGODB_URI)

# Select database
db = client["ai_gym_assistant"]