import os
import sys
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

from src.entity.config import DataTransformationConfig
from src.entity.artifacts import DataIngestionArtifacts, DataTransformationArtifacts
from src.exception import CustomException
from src.logger import logging

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def initiate_data_transformation(
        self, ingestion_artifact: DataIngestionArtifacts
    ) -> DataTransformationArtifacts:
        try:
            logging.info("Starting data transformation...")

            # Load train and test data
            train_df = pd.read_csv(ingestion_artifact.train_file_path)
            test_df = pd.read_csv(ingestion_artifact.test_file_path)

            logging.info("Train and test data loaded")

            # Separate features and target
            X_train = train_df.drop(columns=["Concrete compressive strength(MPa, megapascals) "], axis=1)
            y_train = train_df["Concrete compressive strength(MPa, megapascals) "]

            X_test = test_df.drop(columns=["Concrete compressive strength(MPa, megapascals) "], axis=1)
            y_test = test_df["Concrete compressive strength(MPa, megapascals) "]

            # Scale features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            # Combine scaled features with target
            train_processed = pd.DataFrame(X_train_scaled, columns=X_train.columns)
            train_processed["target"] = y_train.reset_index(drop=True)

            test_processed = pd.DataFrame(X_test_scaled, columns=X_test.columns)
            test_processed["target"] = y_test.reset_index(drop=True)

            # Save transformed data
            train_processed.to_csv(self.config.transformed_train_path, index=False)
            test_processed.to_csv(self.config.transformed_test_path, index=False)
            logging.info("Transformed data saved")

            # Save the preprocessor
            with open(self.config.preprocessor_path, "wb") as f:
                pickle.dump(scaler, f)
            logging.info(" Preprocessor saved")

            return DataTransformationArtifacts(
                transformed_train_path=self.config.transformed_train_path,
                transformed_test_path=self.config.transformed_test_path,
                preprocessor_path=self.config.preprocessor_path,
            )

        except Exception as e:
            raise CustomException(e, sys)
