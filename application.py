import os 
import sys 
from src.Energy_Management_using_Machine_Learning.logger import logging 
from src.Energy_Management_using_Machine_Learning.exception import CustomException
from src.Energy_Management_using_Machine_Learning.components.data_ingestion import DataIngestion

if __name__=="__main__":
    logging.info("Execution has started")

    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)

