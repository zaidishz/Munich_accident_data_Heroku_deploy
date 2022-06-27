import numpy as np
import pandas as pd
from sklearn import preprocessing
from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("model_rf.pkl", "rb"))


@app.route("/", methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    Year = int(request.form.get('Year'))
    Month = int(request.form.get('Month'))
    Category_Alkoholunfälle = int(request.form.get('Category_Alkoholunfälle'))
    Category_Fluchtunfälle = int(request.form.get('Category_Fluchtunfälle'))
    Category_Verkehrsunfälle = int(request.form.get('Category_Verkehrsunfälle'))
    Type_insgesamt = int(request.form.get('Type_insgesamt'))
    #Type_VerletzteundGetötete = int(request.form.get('Type_VerletzteundGetötete'))
    Type_VerletzteundGetötete = 0
    #Type_mitPersonenschäden = int(request.form.get('Type_mitPersonenschäden'))
    Type_mitPersonenschäden = 0
    features = [[Year, Month, Category_Alkoholunfälle, Category_Fluchtunfälle, Category_Verkehrsunfälle, Type_VerletzteundGetötete, Type_insgesamt, Type_mitPersonenschäden]]
    prediction = int(model.predict(features))
    #text = output

    return render_template(
        'index.html',
        prediction_text='prediction value is {}'.format(prediction))


@app.route("/api/predict", methods=["POST"])
def apiPredict():
    if "Year" not in request.get_json() or "Month" not in request.get_json():
        return {"Error": "Year ans Month are required!"}, 400

    data = request.get_json()
    Year = data['Year']
    Month = data['Month']
                            

    if type(Year) != int or Month not in range(1, 13):
        return {"Error": "Input must be a valid number!"}, 400
    else:
        Category_Alkoholunfälle = 1
        Category_Fluchtunfälle = 0
        Category_Verkehrsunfälle = 0
        Type_VerletzteundGetötete = 0
        Type_insgesamt = 1
        Type_mitPersonenschäden = 0
        features = [[Year, Month, Category_Alkoholunfälle, Category_Fluchtunfälle, Category_Verkehrsunfälle, Type_VerletzteundGetötete, Type_insgesamt, Type_mitPersonenschäden]]
        prediction = int(model.predict(features)[0])
        return {'prediction': prediction}


if __name__ == "__main__":
    app.run(debug=True)
