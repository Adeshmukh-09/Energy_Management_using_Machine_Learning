import os 
import sys
import pandas as pd 
from src.Energy_Management_using_Machine_Learning.logger import logging
from src.Energy_Management_using_Machine_Learning.exception import CustomException
from src.Energy_Management_using_Machine_Learning.utils import load_object

class PredictionPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            model_path = os.path.join("Artifacts","model.pkl")
            preprocessor_path = os.path.join("Artifacts","preprocessor.pkl")
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocessor_path)
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)

            return pred
        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self, ambient_temp:float, exhaust_vacuum:float, ambient_pressure:float, relative_humidity:float):
        self.ambient_temp = ambient_temp
        self.exhaust_vacuum = exhaust_vacuum
        self.ambient_pressure = ambient_pressure
        self.relative_humidity = relative_humidity

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "ambient_temp" : [self.ambient_temp],
                "exhaust_vacuum" : [self.exhaust_vacuum],
                "ambient_pressure" : [self.ambient_pressure],
                "relative_humidity" : [self.relative_humidity]
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)


