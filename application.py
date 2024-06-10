import os 
import sys 
from src.Energy_Management_using_Machine_Learning.logger import logging 
from src.Energy_Management_using_Machine_Learning.exception import CustomException
from src.Energy_Management_using_Machine_Learning.components.data_ingestion import DataIngestion
from src.Energy_Management_using_Machine_Learning.components.data_transformation import DataTransformation
from src.Energy_Management_using_Machine_Learning.components.model_training import ModelTrainer

if __name__=="__main__":
    logging.info("Execution has started")

    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        data_transformation = DataTransformation()
        train_arr, test_arr = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr, test_arr))


    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)

