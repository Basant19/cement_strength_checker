from src.entity.config import DataIngestionConfig, DataTransformationConfig
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.entity.config import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


def start_training_pipeline():
    # 1. Data Ingestion
    ingestion_config = DataIngestionConfig.get_default_config()
    data_ingestion = DataIngestion(ingestion_config)
    ingestion_artifacts = data_ingestion.initiate_data_ingestion()

    print(f"Train Data: {ingestion_artifacts.train_file_path}")
    print(f" Test Data: {ingestion_artifacts.test_file_path}")
    print(f" Raw Data: {ingestion_artifacts.raw_file_path}")

    # 2. Data Transformation
    transformation_config = DataTransformationConfig.get_default_config()
    data_transformation = DataTransformation(transformation_config)
    transformation_artifacts = data_transformation.initiate_data_transformation(ingestion_artifacts)

    print(f" Transformed Train: {transformation_artifacts.transformed_train_path}")
    print(f" Transformed Test: {transformation_artifacts.transformed_test_path}")
    print(f" Preprocessor: {transformation_artifacts.preprocessor_path}")

    # 3. Model Training
    trainer_config = ModelTrainerConfig.get_default_config()
    model_trainer = ModelTrainer(trainer_config)
    trainer_artifact = model_trainer.initiate_model_trainer(transformation_artifacts)

    print(f"Model Saved at: {trainer_artifact.trained_model_path}")


if __name__ == "__main__":
    start_training_pipeline()
