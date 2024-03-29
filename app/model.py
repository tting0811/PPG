# -*- coding: UTF-8 -*-
from joblib import dump, load
# 載入模型
RandomForestModel = load('./app/model/best_random_forest_model_4.joblib')

def predict(input):
    pred = RandomForestModel.predict(input)[0]
    print(pred)
    return pred
