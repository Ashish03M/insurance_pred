# Import necessary modules
import os
from pathlib import Path
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

# Define project name
project_name= "Insurance_Pred"

# List of files to be created or checked
list_of_files = [
    f"src/{project_name}/__init__.py",  # Initialization file for project
    f"src/{project_name}/components/__init__.py",  # Initialization file for components submodule
    f"src/{project_name}/components/data_ingestion.py",  # Data ingestion component
    f"src/{project_name}/components/data_transformation.py",  # Data transformation component
    f"src/{project_name}/components/model_trainer.py",  # Model training component
    f"src/{project_name}/components/model_monitoring.py",  # Model monitoring component
    f"src/{project_name}/pipelines/__init__.py",  # Initialization file for pipelines submodule
    f"src/{project_name}/pipelines/training_pipeline.py",  # Training pipeline
    f"src/{project_name}/pipelines/prediction_pipeline.py",  # Prediction pipeline
    f"src/{project_name}/exceptions.py",  # Exception classes
    f"src/{project_name}/logger.py",  # Logging utilities
    f"src/{project_name}/utils.py",  # Utility functions
    "app.py",  # Main application file
    "Dockerfile", # Dockerfile for containerization
    "requirements.txt",
    "setup.py"
]

# Loop through each file path in the list
for filepath in list_of_files:
    # Convert file path to a Path object
    filepath = Path(filepath)
    # Split file path into directory and filename
    filedir, filename = os.path.split(filepath)

    # Check if directory is specified
    if filedir != "":
        # Create directory if it doesn't exist
        os.makedirs(filedir, exist_ok=True)
        # Log directory creation
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Check if file doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create an empty file
        with open(filepath, 'w') as f:
            pass
        # Log empty file creation
        logging.info(f"Creating empty file: {filepath}")

    else:
        # Log if file already exists
        logging.info(f"{filename} already exists")
