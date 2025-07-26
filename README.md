#  Cement Strength Prediction - Machine Learning Pipeline

This project predicts the **compressive strength of concrete** based on its ingredients using a complete end-to-end **Machine Learning pipeline** including:

- Data ingestion from **MongoDB**
- Data preprocessing and transformation
- Model training with hyperparameter tuning
- Model evaluation and visualization
- Dockerized application deployment using **AWS App Runner**
- CI/CD pipeline using **GitHub Actions + Docker + ECR**

---



The model uses **Gradient Boosting Regressor** with **GridSearchCV** for hyperparameter optimization.

---

# Start full training pipeline
python src/pipeline/training_pipeline.py


---
# How to Run the Project

1. Clone the Repository
git clone https://github.com/your-username/cement_strength_prediction.git
cd cement_strength_prediction

2. Create and Activate a Virtual Environment
#use Python 3.10.0
python -m venv venv
source venv/bin/activate         # For Linux/Mac
venv\Scripts\activate            # For Windows

3. Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

4. Set Environment Variables
MONGO_URI=your_mongo_connection_uri
Ensure the database and collection are:

Database: cement_strength

Collection: strength_data

5. Run the Training Pipeline
python src/pipeline/training_pipeline.py

This will:

Ingest data from MongoDB

Perform data transformation

Train the model

Save model artifacts in the artifacts/ directory

6. Run the Flask App (Locally)

python app.py


---
## some instruction for dependency conflicts errors 
1)🔍 Analyze with pipdeptree

pip install pipdeptree
pipdeptree
*Visualizes the dependency tree and helps detect conflicts or unnecessary packages.

2)List all currently installed packages use pip freeze 

