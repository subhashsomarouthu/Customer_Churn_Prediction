import pickle
import numpy as np

def load_model():
    global svm_model
    with open("SVM_model.pkl",'rb') as f:
        svm_model=pickle.load(f)
    print("Loaded SVM Model")
def predict(features_dict):
    if svm_model is None:
        raise ValueError("Model is not loaded. Call load_model() first.")
    feature_names = ["REST_AVG_CUR",
                     "LDEAL_ACT_DAYS_PCT_AAVG",
                     "REST_DYNAMIC_IL_3M",
                     "CR_PROD_CNT_IL_5",
                     "CR_PROD_CNT_TOVR_4",
                     "REST_DYNAMIC_CUR_1M",
                     "CR_PROD_CNT_TOVR_5",
                     "CR_PROD_CNT_PIL_4",
                     "TURNOVER_DYNAMIC_IL_3M",
                     "TURNOVER_DYNAMIC_IL_1M",
                     "APP_MARITAL_STATUS_Civil Union",
                     "CR_PROD_CNT_CC_9",
                     "PACK_109",
                     "CR_PROD_CNT_VCU_3",
                     "CR_PROD_CNT_TOVR_6"]

    feature_vector = [features_dict.get(name, 0) for name in feature_names]
    feature_array = np.array(feature_vector).reshape(1, -1)
    prediction = svm_model.predict(feature_array)
    return prediction[0]

load_model()