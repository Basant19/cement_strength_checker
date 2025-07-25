import os
import sys
import pandas as pd
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv

from src.entity.config import DataIngestionConfig
from src.entity.artifacts import DataIngestionArtifacts
from src.exception import CustomException
from src.logger import logging

# Load .env file
load_dotenv()

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        self.mongo_uri = os.getenv("MONGO_URI")

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        try:
            logging.info("Starting Data Ingestion from MongoDB...")

            # Create directories
            os.makedirs(self.config.raw_data_dir, exist_ok=True)
            os.makedirs(os.path.dirname(self.config.train_file_path), exist_ok=True)

            # Connect to MongoDB
            client = MongoClient(self.mongo_uri)
            db = client["cement_strength"]               
            collection = db["strength_data"]     

            # Fetch data from MongoDB and convert to DataFrame
            data = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB default _id field
            df = pd.DataFrame(data)

            logging.info(" Data fetched from MongoDB successfully")

            # Save raw data
            df.to_csv(self.config.raw_file_path, index=False)
            logging.info(f" Raw data saved at {self.config.raw_file_path}")

            # Train/test split
            train_df, test_df = train_test_split(df, test_size=self.config.test_size, random_state=42)
            train_df.to_csv(self.config.train_file_path, index=False)
            test_df.to_csv(self.config.test_file_path, index=False)

            logging.info("Train/test data saved")

            return DataIngestionArtifacts(
                train_file_path=self.config.train_file_path,
                test_file_path=self.config.test_file_path,
                raw_file_path=self.config.raw_file_path
            )

        except Exception as e:
            raise CustomException(e, sys)
