import os
import sys
import joblib  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from pathlib import Path

from src.exception import CustomException
from src.logger import logging

# Paths
MODEL_PATH = Path("artifacts/model.pkl")
TEST_DATA_PATH = Path("artifacts/transformed_test.csv")
PLOT_PATH = Path("artifacts/evaluation_plot.png")


def load_test_data():
    try:
        df = pd.read_csv(TEST_DATA_PATH)
        logging.info(f"Test data loaded from: {TEST_DATA_PATH}")
        X_test = df.drop(columns=["target"])
        y_test = df["target"]
        return X_test, y_test
    except Exception as e:
        logging.error("Error loading test data")
        raise CustomException(e, sys)


def load_model():
    """
    Load the trained model using joblib.
    """
    try:
        model = joblib.load(MODEL_PATH)
        logging.info(f"Model loaded from: {MODEL_PATH}")
        return model
    except Exception as e:
        logging.error("Error loading model")
        raise CustomException(e, sys)


def evaluate_model(model, X_test, y_test):
    try:
        y_pred = model.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        logging.info(f"Evaluation Metrics — MSE: {mse:.2f}, RMSE: {rmse:.2f}, MAE: {mae:.2f}, R²: {r2:.2f}")

        print("\nEvaluation Metrics:")
        print(f"Mean Squared Error (MSE): {mse:.2f}")
        print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
        print(f"Mean Absolute Error (MAE): {mae:.2f}")
        print(f"R² Score: {r2:.2f}")

        return y_pred, mse, rmse, mae, r2
    except Exception as e:
        logging.error("Error during model evaluation")
        raise CustomException(e, sys)


def plot_results(y_test, y_pred):
    try:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=y_test, y=y_pred)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--', color='red')
        plt.xlabel("Actual Compressive Strength")
        plt.ylabel("Predicted Compressive Strength")
        plt.title("Actual vs Predicted Compressive Strength")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(PLOT_PATH)
        logging.info(f"Evaluation plot saved at: {PLOT_PATH}")
        print(f"Plot saved at: {PLOT_PATH}")
        plt.show()
    except Exception as e:
        logging.error("Error while plotting results")
        raise CustomException(e, sys)


if __name__ == "__main__":
    try:
        X_test, y_test = load_test_data()
        model = load_model()
        y_pred, mse, rmse, mae, r2 = evaluate_model(model, X_test, y_test)
        plot_results(y_test, y_pred)
    except Exception as e:
        logging.critical("Unexpected error occurred during model evaluation")
        raise CustomException(e, sys)
