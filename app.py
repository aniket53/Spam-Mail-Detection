import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

#Start of our application
app = Flask(__name__)

#Load our model
spamDetectModel= pickle.load(open('spammodel.pkl','rb'))
feature_extractor=pickle.load(open('feature_extraction.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data'] #receive the data and store it in data object.
    new_data=feature_extractor.transform(np.array([data]))
    output=spamDetectModel.predict(new_data)[0]
    print(output)
    if output==1:
        return "The given mail is a HAM mail."
    else:
        return "The given mail is a SPAM mail."   

@app.route('/predict',methods=['POST'])
def predict():
    data=request.form.values()
    standardize_input= feature_extractor.transform(data)
    output=spamDetectModel.predict(standardize_input)[0]
    if output==1:
        return render_template("home.html",predicted_text="HAM mail")
    else:
        return render_template("home.html",predicted_text="SPAM mail")


if __name__=="__main__":
    app.run(debug=True)

