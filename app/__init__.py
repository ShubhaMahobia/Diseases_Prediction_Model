from flask import Flask, jsonify, request
import numpy as np
import pickle
import sklearn
import os
print("Current working directory:", os.getcwd())
file_path = './NBmodel.pkl'

if os.path.isfile(file_path):
    print("File exists")
else:
    print("File does not exist")

model = pickle.load(open('NBmodel.pkl', 'rb'))

# Call the 'predict' method on the model
# prediction = model.predict(input_data)

app = Flask(__name__)   

@app.route('/')
def welcome():
    return "ML Server is running"

@app.route('/predict', methods=["POST"])
def predict():
    data = request.json
    # Extracting features from JSON data
    features = np.array([[data['s1'], data['s2'], data['s3'], data['s4'], data['s5'],
                          data['s6'], data['s7'], data['s8'], data['s9'], data['s10']]])
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)