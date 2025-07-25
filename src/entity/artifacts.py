from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    train_file_path: str
    test_file_path: str
    raw_file_path: str

@dataclass
class DataTransformationArtifacts:
    transformed_train_path: str
    transformed_test_path: str
    preprocessor_path: str

@dataclass
class ModelTrainerArtifacts:
    trained_model_path: str
