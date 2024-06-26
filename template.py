import os 
import logging 
from pathlib import Path

logging.basicConfig(level = logging.INFO)
project_name = "Energy_Management_using_Machine_Learning"

list_of_path = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_training.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "application.py",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_path:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok= True)
        logging.info(f"Creating Directory:{filedir} for the file:{filename}")

    if ((not os.path.exists(filepath)) or (os.path.getsize(filepath)==0)):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating new file:{filepath}") 
    
    else:
        logging.info(f"{filename} already exist")

