from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model (replace 'model.pkl' with your model file)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_churn():
    try:
        # Get input values from the form
        credit_product_count = float(request.form.get('credit-product-count', 0))
        turnover_payment = float(request.form.get('turnover-payment', 0))
        credit_card_count = float(request.form.get('credit-card-count', 0))
        transaction_count_supermarket = float(request.form.get('transaction-count-supermarket', 0))
        turnover_dynamic_cur_1m = float(request.form.get('turnover-dynamic-cur-1m', 0))
        turnover_dynamic_cur_3m = float(request.form.get('turnover-dynamic-cur-3m', 0))
        client_setup_tenure = float(request.form.get('client-setup-tenure', 0))
        rest_average_current = float(request.form.get('rest-average-current', 0))
        credit_product_count_tovr = float(request.form.get('credit-product-count-tovr', 0))
        rest_average_payment = float(request.form.get('rest-average-payment', 0))

        # Create a feature array for prediction
        features = np.array([[credit_product_count, turnover_payment, credit_card_count,
                              transaction_count_supermarket, turnover_dynamic_cur_1m,
                              turnover_dynamic_cur_3m, client_setup_tenure, rest_average_current,
                              credit_product_count_tovr, rest_average_payment] +
                             [0] * (36 - 10)])  # Fill remaining features with zeros

        # Make a prediction
        prediction = model.predict(features)

        # Determine the result and color
        if prediction[0] == 1:
            result = 'The customer is likely to churn.'
            color = 'green'
        else:
            result = 'The customer is not likely to churn.'
            color = 'red'

    except Exception as e:
        result = 'Error: ' + str(e)
        color = 'orange'  # You can choose a different color for error messages

    return render_template('index.html', result=result, color=color)


if __name__ == '__main__':
    app.run(debug=True)
