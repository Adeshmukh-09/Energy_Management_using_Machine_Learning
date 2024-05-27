import os 
import sys 
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.Energy_Management_using_Machine_Learning.logger import logging 
from src.Energy_Management_using_Machine_Learning.exception import CustomException

@dataclass

class DataIngestionConfig:
 raw_data_path:str = os.path.join("Artifacts","raw.csv")
 train_data_path:str = os.path.join("Artifacts","train_data.csv")
 test_data_path:str = os.path.join("Artifacts","test_data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Reading the raw data from CSV file")

            data =  pd.read_csv("D:\\Data Science Roadmap and Practice\\Machine Learning Projects\\Energy_Management_using_Machine_Learning\\notebook\\Data\\energy_plant_data.csv")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok= True)
            data.to_csv(self.ingestion_config.raw_data_path,index = False,header = True)
            logging.info("raw data file has been created")

            logging.info("Splitting the Data into training and test data")
            train_data, test_data = train_test_split(data, test_size=0.20, random_state=42)

            train_data.to_csv(self.ingestion_config.train_data_path,index= False, header = True)
            logging.info("training data file has been created")

            test_data.to_csv(self.ingestion_config.test_data_path,index = False, header = True)
            logging.info("test data file has been created")

            logging.info("data ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )



        except Exception as e:
            raise CustomException(e,sys)



 




