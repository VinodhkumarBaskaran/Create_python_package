import os
from pathlib import Path
import logging

# list of files and folder required for project development
list_of_files =[
    
    ".github/workflows/.gitkeep",    # CI/CD --> Continuous Integration and Continuous Deployment
    "src/__init__.py",
    
    "src/components/__init__.py", # Step by step components of ML project
    "src/components/data_injection.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/data_evaluation.py",
    
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    
    "src/utils/__init__.py",
    "src/utils/utils.py",
    
    "src/logger/logging.py",
    "src/exception/exception.py", # testing logic and other snippnets
    
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    
    "init_setup.sh",
    
    "requirement.txt",
    "requirement_dev.txt",

    "setup.py",
    "setup.cfg",
    
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]


for filepath in list_of_files:
    filepath = Path(filepath) # a/b/c.txt
    filedir, filename = os.path.split(filepath)  # filedir = a/b   filename = c.txt
    
    if filedir != "": # file directory is not empty
        os.makedirs(filedir, exist_ok=True) # then create a file directory
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # if filesize is zero or not represent
        with open(filepath, "w") as f:
            pass # Create an empyt file