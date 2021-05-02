import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/predict')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['article']
    data = [text]
    prediction = model.predict(data)
    if (prediction[0]==0):
        return render_template('index.html', prediction_text='Business Article')
    elif (prediction[0]==1):
        return render_template('index.html', prediction_text='Entertainment Article')    
    else:
        return render_template('index.html', prediction_text='Technology Article')

@app.route('/result',methods=['POST'])
def result():
    data = request.get_json(force=True)
    data = [data]
    prediction = model.predict(data)
    output = prediction[0]
    return jsonify(output)            
if __name__ == "__main__":
    app.run(debug=True)
