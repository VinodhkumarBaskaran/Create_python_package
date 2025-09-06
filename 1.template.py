import os
from pathlib import Path
import logging

package_name = "mongodb_connect"

# list of files and folder required for project development
list_of_files = [
   ".github/workflows/ci.yaml",
   "src/__init__.py",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/mongo_crud.py", 
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/unit/unit.py",
   "tests/integration/__init__.py",
   "tests/integration/int.py",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb", 
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