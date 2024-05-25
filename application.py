import os 
import sys 
from src.Energy_Management_using_Machine_Learning.logger import logging 
from src.Energy_Management_using_Machine_Learning.exception import CustomException

if __name__=="__main__":
    logging.info("Execution has started")

    try:
        a = 1/0

    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)

