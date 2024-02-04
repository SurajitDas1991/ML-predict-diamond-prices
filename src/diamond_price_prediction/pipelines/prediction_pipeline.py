import sys
import os
from diamond_price_prediction.exception import CustomException
from diamond_price_prediction.logger import logging
from diamond_price_prediction.utils import load_object
import pandas as pd
from pydantic import BaseModel

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)
            return pred

        except Exception as e:
            logging.info("Exception occurred in prediction")
            raise CustomException(e, sys) # type: ignore




class CustomData(BaseModel):
    carat:float
    cut: str
    color: str
    clarity: str
    depth:float
    table: float
    x: float
    y: float
    z: float
    
    
def get_data_as_dataframe(custom_data_input_dict:CustomData):
    try:
        df=pd.DataFrame.from_dict([dict(custom_data_input_dict)])
        #df = pd.DataFrame(dict(custom_data_input_dict))
        logging.info("Dataframe Gathered")
        return df
    except Exception as e:
        logging.info("Exception Occurred in prediction pipeline")
        raise CustomException(e, sys)  # type: ignore

    # def get_data_as_dataframe(self):
    #     try:
    #         custom_data_input_dict = {
    #             "carat": [self.carat],
    #             "depth": [self.depth],
    #             "table": [self.table],
    #             "x": [self.x],
    #             "y": [self.y],
    #             "z": [self.z],
    #             "cut": [self.cut],
    #             "color": [self.color],
    #             "clarity": [self.clarity],
    #         }
    #         df = pd.DataFrame(custom_data_input_dict)
    #         logging.info("Dataframe Gathered")
    #         return df
    #     except Exception as e:
    #         logging.info("Exception Occurred in prediction pipeline")
    #         raise CustomException(e, sys) # type: ignore
