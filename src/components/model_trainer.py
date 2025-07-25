# src/components/model_trainer.py

import os
import sys
import joblib
import numpy as np
from dataclasses import dataclass
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException
from src.logger import logging
from src.entity.config import ModelTrainerConfig
from src.entity.artifacts import DataTransformationArtifacts, ModelTrainerArtifacts


@dataclass
class ModelTrainerConfig:
    trained_model_path: str = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig = ModelTrainerConfig()):
        self.config = config

    def initiate_model_trainer(
        self, transformation_artifact: DataTransformationArtifacts
    ) -> ModelTrainerArtifacts:
        try:
            logging.info("Loading transformed train and test datasets")

            train_df = joblib.load(transformation_artifact.transformed_train_path) \
                       if transformation_artifact.transformed_train_path.endswith(".pkl") \
                       else None
            test_df  = joblib.load(transformation_artifact.transformed_test_path)  \
                       if transformation_artifact.transformed_test_path.endswith(".pkl") \
                       else None

            # Fallback to CSV
            if train_df is None:
                import pandas as pd
                train_df = pd.read_csv(transformation_artifact.transformed_train_path)
                test_df  = pd.read_csv(transformation_artifact.transformed_test_path)

            X_train, y_train = train_df.drop("target", axis=1), train_df["target"]
            X_test,  y_test  = test_df.drop("target", axis=1),  test_df["target"]

            # Hyperparameter grid
            param_grid = {
                "n_estimators": [100, 200],
                "learning_rate": [0.01, 0.1],
                "max_depth": [3, 5],
                "min_samples_split": [2, 4],
                "min_samples_leaf": [1, 2],
            }

            gb = GradientBoostingRegressor(random_state=42)
            grid = GridSearchCV(
                estimator=gb,
                param_grid=param_grid,
                scoring="neg_mean_squared_error",
                cv=3,
                n_jobs=-1,
                verbose=1,
            )

            logging.info("Starting GridSearchCV for GradientBoostingRegressor")
            grid.fit(X_train, y_train)

            best_model = grid.best_estimator_
            logging.info(f"Best parameters: {grid.best_params_}")

            # Evaluate
            preds = best_model.predict(X_test)
            mse  = mean_squared_error(y_test, preds)
            rmse = np.sqrt(mse)
            r2   = r2_score(y_test, preds)

            logging.info(f"Evaluation—MSE: {mse:.2f}, RMSE: {rmse:.2f}, R²: {r2:.2f}")

            # Ensure artifact directory exists
            os.makedirs(os.path.dirname(self.config.trained_model_path), exist_ok=True)

            # Save model
            joblib.dump(best_model, self.config.trained_model_path)
            logging.info(f"Saved trained model at {self.config.trained_model_path}")

            return ModelTrainerArtifacts(trained_model_path=self.config.trained_model_path)

        except Exception as e:
            raise CustomException(e, sys)
