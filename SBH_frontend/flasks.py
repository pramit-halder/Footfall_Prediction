import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import metrics
from flask import Flask,request,render_template,jsonify
from flask_cors import CORS

import pickle

#creating an instance of flask
app = Flask(__name__)

#CHANGE :here link of react app will be given
CORS(app,origins=["http://localhost:3000"])


@app.route("/",methods=['POST'])
def home():
    # CHANGE : csv file ours should be given 
    dataset_url="Dataset\winequality-red.csv" 
    dataread = pd.read_csv(dataset_url)

    

    #taking the data

    # CHANGE :model is loaded from .sav file using pickle 
    load_model=pickle.load(open("model.sav","rb"))

    # converting Date in String and putting it in array
    # do this part whichever way you like , similar the way you do it for hardcore backend
    input_datas = [str(Date)]
    input_array =np.array(input_datas)
    input_datas_reshaped = input_array.reshape(1,-1)
    predictions = load_model.predict(input_datas_reshaped)

    print(predictions)

    # do whatever you wanna do with the prediciton , and pass it as string 
    #put it in output variable

    if (predictions[0] == 1):
        output ="Good" 
    else:
        output ="Bad"
    # dont touch return part

    return jsonify(output)



# Running app
if __name__ == '__main__':
    app.run(debug=True)