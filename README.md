
# Bank Customer Churn Prediction

This project aims to predict customer churn for a bank using machine learning models. The dataset contains information about the bank's customers and various features related to their transactions, demographics, and account activity. The main objective is to build and tune machine learning models to accurately predict whether a customer will churn or not.

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Data Preprocessing](#data-preprocessing)
4. [Feature Engineering](#feature-engineering)
5. [Model Training and Tuning](#model-training-and-tuning)
6. [Model Evaluation](#model-evaluation)
7. [Interpretability](#interpretability)
8. [Deployment](#deployment)
9. [Usage](#usage)
10. [Results](#results)
11. [Conclusion](#conclusion)

## Introduction
Customer churn is a critical issue for banks, as retaining existing customers is often more cost-effective than acquiring new ones. This project leverages machine learning to predict which customers are likely to churn based on their historical data and behavior patterns.

## Dataset
The dataset consists of 355,190 rows and 116 columns, including demographic information, transaction history, and other customer-related data. The target variable is `TARGET`, indicating whether a customer has churned (1) or not (0).

## Data Preprocessing
Data preprocessing steps included:
- Handling missing values
- Removing duplicate entries
- Converting categorical variables to numerical format using one-hot encoding
- Normalizing numerical features
- Splitting the data into training and test sets

## Feature Engineering
Significant features were identified through various techniques, including correlation analysis, SHAP, and LIME. The top features selected for the model included:
- `REST_AVG_CUR`
- `LDEAL_ACT_DAYS_PCT_AAVG`
- `REST_DYNAMIC_IL_3M`
- `CR_PROD_CNT_IL_5`
- `CR_PROD_CNT_TOVR_4`
- `REST_DYNAMIC_CUR_1M`
- `CR_PROD_CNT_TOVR_5`
- `CR_PROD_CNT_PIL_4`
- `TURNOVER_DYNAMIC_IL_3M`
- `TURNOVER_DYNAMIC_IL_1M`
- `APP_MARITAL_STATUS_Civil Union`
- `CR_PROD_CNT_CC_9`
- `PACK_109`
- `CR_PROD_CNT_VCU_3`
- `CR_PROD_CNT_TOVR_6`

## Model Training and Tuning
The models trained and tuned include:
- Logistic Regression
- Support Vector Machine (SVM)

Hyperparameter tuning was performed using grid search and cross-validation to optimize model performance. The models were evaluated based on various metrics such as accuracy, precision, recall, F1 score, AUC score.


  

## Interpretability
The interpretability of the models was analyzed using LIME. These methods provided insights into the most important features driving the predictions:

- LIME (Local Interpretable Model-agnostic Explanations) was used to explain individual predictions by approximating the model locally.

## Deployment
The final models were deployed using Flask and Gunicorn, with a user interface built using Streamlit. This setup allows users to input customer data and receive a churn prediction in real-time.

## Usage
To run the project locally:
1. Clone the repository.
2. Install the required dependencies.
3. Run the Flask app using Gunicorn.
4. Access the Streamlit interface to input customer data and view predictions.

## Results
The models successfully predicted customer churn with reasonable accuracy. The SVM model outperformed Logistic Regression in terms of recall and F1 score, making it a better choice for identifying potential churners.

## Conclusion
This project demonstrates the effectiveness of machine learning in predicting customer churn. By understanding the key features contributing to churn, banks can develop targeted strategies to retain customers and reduce churn rates.

