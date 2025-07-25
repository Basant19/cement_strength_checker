import os
from pymongo import MongoClient
from dotenv import load_dotenv
from src.logger import logging

# Load environment variables
load_dotenv()

def test_mongodb_connection():
    try:
        uri = os.getenv("MONGO_URI")
        if uri is None:
            raise ValueError("MONGO_URI is not set in the .env file")

        client = MongoClient(uri)
        logging.info("✅ Successfully connected to MongoDB")

        # List databases
        db_list = client.list_database_names()
        logging.info(f"📁 Databases in your MongoDB account: {db_list}")

        for db_name in db_list:
            db = client[db_name]
            collection_list = db.list_collection_names()
            logging.info(f"📂 Collections in '{db_name}': {collection_list}")

    except Exception as e:
        logging.error(f"❌ MongoDB connection failed: {str(e)}")
        raise e

if __name__ == "__main__":
    test_mongodb_connection()
    print("✅ MongoDB connection verified. Check logs for full details.")

