import streamlit as st
from diamond_price_prediction.pipelines.prediction_pipeline import CustomData,PredictPipeline
import requests
import json
#from diamond_price_prediction import application
# interact with FastAPI endpoint
#backend = "http://localhost:8080/predict_price"
backend = "http://fast_api:9080/predict_price"


    
st.title("Diamond Price Prediction")

st.divider()

carat_value = st.number_input("CARAT", value=None, placeholder="Type a number...")

cut_value = st.text_input("CUT", value="")

color_value = st.text_input("COLOR", value="")

clarity_value = st.text_input("CLARITY", value="")

depth_value = st.number_input("DEPTH", value=None, placeholder="Type a number...")

table_value = st.number_input("TABLE", value=None, placeholder="Type a number...")

x_value = st.number_input("X", value=None, placeholder="Type a number...")

y_value = st.number_input("Y", value=None, placeholder="Type a number...")

z_value = st.number_input("Z", value=None, placeholder="Type a number...")


if st.button("Predict Price"):
    dict_of_user_entry_values={
        "carat":carat_value,
        "cut":cut_value,
        "color":color_value,
        "clarity":clarity_value,
        "depth":depth_value,
        "table":table_value,
        "x":x_value,
        "y":y_value,
        "z":z_value
    }
    #print(dict_of_user_entry_values)
    #st.write(type(dict_of_user_entry_values))
    json_object = json.dumps(dict_of_user_entry_values) 
    #print(dict_of_user_entry_values)
    headers = {
                'Content-Type': 'application/json'
                }
    result=requests.post(url=backend,data=json_object,headers=headers)
    # result=application.predict_diamond_price(dict_of_user_entry_values)
    st.write(result.text)
