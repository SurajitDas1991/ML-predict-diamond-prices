import os
import sys
from diamond_price_prediction.logger import logging
from diamond_price_prediction.exception import CustomException
import pandas as pd

from diamond_price_prediction.components.data_ingestion import DataIngestion
from diamond_price_prediction.components.data_transformation import DataTransformation

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    print(train_data_path, test_data_path)
    data_transformation = DataTransformation()

    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
        train_data_path, test_data_path
    )
