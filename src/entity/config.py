import os
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_dir: str
    raw_file_path: str
    train_file_path: str
    test_file_path: str
    test_size: float

    @staticmethod
    def get_default_config(base_dir: str = "artifacts") -> "DataIngestionConfig":
        raw_data_dir = os.path.join(base_dir, "raw_data")
        return DataIngestionConfig(
            raw_data_dir=raw_data_dir,
            raw_file_path=os.path.join(raw_data_dir, "raw.csv"),
            train_file_path=os.path.join(base_dir, "train.csv"),
            test_file_path=os.path.join(base_dir, "test.csv"),
            test_size=0.2
        )

@dataclass
class DataTransformationConfig:
    transformed_train_path: str
    transformed_test_path: str
    preprocessor_path: str

    @staticmethod
    def get_default_config(base_dir: str = "artifacts") -> "DataTransformationConfig":
        return DataTransformationConfig(
            transformed_train_path=os.path.join(base_dir, "transformed_train.csv"),
            transformed_test_path=os.path.join(base_dir, "transformed_test.csv"),
            preprocessor_path=os.path.join(base_dir, "preprocessor.pkl"),
        )

@dataclass
class ModelTrainerConfig:
    trained_model_path: str

    @staticmethod
    def get_default_config(base_dir: str = "artifacts") -> "ModelTrainerConfig":
        return ModelTrainerConfig(
            trained_model_path=os.path.join(base_dir, "model.pkl")
        )
