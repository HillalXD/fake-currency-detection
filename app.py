from flask import Flask, request, jsonify
from flasgger import Swagger
import pickle

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/")
def hello():
  return "Hello World"

@app.route('/predict', methods=['POST'])
def predict():
    """
    ---
    parameters:
      - name: variance
        in: formData
        type: number
        description: value of currency variance
        required: true
      - name: skewness
        in: formData
        type: number
        description: value of currency skewness
        required: true
      - name: curtosis
        in: formData
        type: number
        description: value of currency curtosis
        required: true
      - name: entropy
        in: formData
        type: number
        description: value of currency entropy
        required: true
    responses:
      200:
        description: The predicted currency condition.
    """
    # Load the machine learning model
    model = pickle.load(open('knearest.pkl', "rb"))

    # Get the values from the form
    var = float(request.form['variance'])
    skew = int(request.form['skewness'])
    cur = int(request.form['curtosis'])
    ent = float(request.form['entropy'])

    # Make a prediction
    prediction = model.predict([[var, skew, cur, ent]])

    # Return the prediction as JSON
    if prediction == 1:
        return "currency is fake"
    else:
        return "currency is good"


if __name__ == '__main__':
    app.run(debug=True)
