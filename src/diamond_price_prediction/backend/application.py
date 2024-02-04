from fastapi import FastAPI
from diamond_price_prediction.pipelines.prediction_pipeline import CustomData,PredictPipeline,get_data_as_dataframe
import uvicorn

app=FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}

@app.post('/predict_price')
def predict_diamond_price(dict_of_values:CustomData):
    #print(dict_of_values)
    final_new_data=get_data_as_dataframe(dict_of_values)
    #final_new_data=data.get_data_as_dataframe()
    predict_pipeline=PredictPipeline()
    pred=predict_pipeline.predict(final_new_data)

    results=round(pred[0],2)
    #print(results)
    return results


if __name__ == "__main__":
    uvicorn.run("application:app", host="0.0.0.0", port=9080,reload=True)
