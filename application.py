import os 
import sys 
from src.Energy_Management_using_Machine_Learning.logger import logging 
from src.Energy_Management_using_Machine_Learning.exception import CustomException
from src.Energy_Management_using_Machine_Learning.components.data_ingestion import DataIngestion
from src.Energy_Management_using_Machine_Learning.components.data_transformation import DataTransformation
from src.Energy_Management_using_Machine_Learning.components.model_training import ModelTrainer
from src.Energy_Management_using_Machine_Learning.pipelines.prediction_pipeline import CustomData, PredictionPipeline
from flask import render_template, request, Flask

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predictdata', methods = ["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")
    else:
        data = CustomData(
            ambient_temp = request.form.get("ambient_temp"),
            exhaust_vacuum = request.form.get("exhaust_vacuum"),
            ambient_pressure = request.form.get("ambient_pressure"),
            relative_humidity = request.form.get("relative_humidity")
        )

        pred_df = data.get_data_as_dataframe()
        print(pred_df)
        predidct_pipeline = PredictionPipeline()
        pred = predidct_pipeline.predict(pred_df)
        result = pred
        return render_template('home.html',final_result = result)


if __name__=="__main__":
    logging.info("Execution has started")

    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        data_transformation = DataTransformation()
        train_arr, test_arr = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr, test_arr))
        app.run(host = "0.0.0.0", port = 7070)


    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)

