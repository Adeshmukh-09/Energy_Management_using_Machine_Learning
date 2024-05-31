import os
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
from src.Energy_Management_using_Machine_Learning.logger import logging
from src.Energy_Management_using_Machine_Learning.exception import CustomException
from src.Energy_Management_using_Machine_Learning.utils import save_object

@dataclass

class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("Artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_obj(self):
        try:
            logging.info("data transformation has started")

            numerical_columns = ["ambient_temp", "exhaust_vacuum", "ambient_pressure", "relative_humidity"]

            numerical_pipeline = Pipeline(steps= [
                ('imputer',SimpleImputer(strategy= "median")),
                ('standardscaler',StandardScaler())
                ])
            
            logging.info(f"numerical columns are: {numerical_columns}")

            preprocessor = ColumnTransformer(
                transformers=[("numerical_pipeline", numerical_pipeline, numerical_columns)]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('reading the train and test data done')

            preprocessor_obj = self.get_data_transformer_obj()

            target_column = "electrical_energy"

            input_feature_train_df = train_df.drop(columns= target_column, axis =1)
            target_feature_train_df = train_df.loc[:,[target_column]]

            input_feature_test_df = test_df.drop(columns = target_column, axis=1)
            target_feature_test_df = test_df.loc[:,[target_column]]

            logging.info('Applying preprocessor on the train and test data')

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df )]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df )]

            logging.info('ssaving preprocessor file')

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            )

            return(
                train_arr,
                test_arr
            )


        except Exception as e:
            raise CustomException(e,sys)