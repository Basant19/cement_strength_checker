import os

# List of folders to create
folders = [
    ".github/workflows",
    "config",
    "notebook",
    "src/components",
    "src/pipeline",
    "src/utils",
    "src/entity",
    "tests",
    "static",
    "templates",
    "artifacts",
    "logs"
]

# List of files to create
files = [
    ".github/workflows/cicd.yaml",
    ".gitignore",
    "application.py",
    "app.py",
    "Dockerfile",
    ".dockerignore",
    "README.md",
    "requirements.txt",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
    "config/constants.py",
    "src/__init__.py",
    "src/logger.py",
    "src/exception.py",
    "src/entity/__init__.py",
    "src/entity/config.py",
    "src/entity/artifacts.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/pipeline/__init__.py",
    "src/pipeline/train_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/main_utils.py",
    "tests/test_data_ingestion.py",
    "tests/test_model_trainer.py"
]

def create_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"✅ Created folder: {folder}")

    for file in files:
        with open(file, "w") as f:
            f.write("#generated file\n")
        print(f"📄 Created file: {file}")

if __name__ == "__main__":
    print("🚀 Starting project structure generation...")
    create_structure()
    print("✅ Project structure generated successfully.")
