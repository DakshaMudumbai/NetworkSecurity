import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_db_url = os.getenv("MONGO_DB_URL")
if not mongo_db_url:
    mongo_db_url = os.getenv("MONGODB_URL_KEY")

print(f"Testing connection with: {mongo_db_url[:20]}...")

try:
    client = MongoClient(mongo_db_url)
    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
