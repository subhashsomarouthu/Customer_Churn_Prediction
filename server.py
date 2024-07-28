from flask import Flask, jsonify, render_template, request
import util
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_churn', methods=['GET','POST'])

def predict():
    data = request.get_json()
    res = util.predict(data)
    return str(res)


if __name__ == '__main__':
    app.run(debug=True)
