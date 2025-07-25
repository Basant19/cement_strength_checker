import os
import pandas as pd
import json
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from src.logger import logging  # ✅ Use centralized logger

# Load .env variables
load_dotenv()

def upload_csv_to_mongodb(csv_file_path: str, database_name: str, collection_name: str):
    try:
        uri = os.getenv("MONGO_URI")

        if uri is None:
            raise Exception("MONGO_URI is not set in the .env file")

        # Connect to MongoDB
        client = MongoClient(uri)
        logging.info("MongoDB connection established successfully.")

        # Load CSV
        df = pd.read_csv(csv_file_path)
        logging.info(f"CSV loaded successfully from {csv_file_path} with shape {df.shape}.")

        # Convert to JSON records
        json_records = list(json.loads(df.T.to_json()).values())

        # Upload to MongoDB
        client[database_name][collection_name].insert_many(json_records)
        logging.info(f"Inserted {len(json_records)} records into {database_name}.{collection_name}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise e

if __name__ == "__main__":
    csv_path = r"D:\pw_internship_project\cement_strength_prediction\notebook\cement_data.csv"
    upload_csv_to_mongodb(csv_path, database_name="cement_strength", collection_name="strength_data")
    print("✅ CSV data uploaded to MongoDB successfully check logs folder to verify .")