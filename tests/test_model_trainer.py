import os
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig
from src.entity.artifacts import DataTransformationArtifacts

def test_model_trainer():
    artifact = DataTransformationArtifacts(
        transformed_train_path="artifacts/transformed_train.csv",
        transformed_test_path="artifacts/transformed_test.csv",
        preprocessor_path="artifacts/preprocessor.pkl"
    )
    config = ModelTrainerConfig()
    trainer = ModelTrainer(config)
    output = trainer.initiate_model_trainer(artifact)

    assert os.path.exists(output.trained_model_path), "Model file was not created"
    print(f"Test Passed: Model saved at {output.trained_model_path}")

if __name__ == "__main__":
    test_model_trainer()
