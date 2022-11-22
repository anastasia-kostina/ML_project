from flask import Flask, request, jsonify
import dill


import pandas as pd
import numpy as np

from sklift.metrics import uplift_at_k
from sklift.viz import plot_uplift_preds
from sklift.models import SoloModel

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklift.datasets import fetch_lenta
from sklearn.model_selection import train_test_split


from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion, make_pipeline

import dill

dill._dill._reverse_typemap['ClassType'] = type


with open('solomodel_pipeline.dill', 'rb') as in_strm:
    pipeline = dill.load(in_strm)

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def general():
    return "Welcom to prediction process"


@app.route("/predict", methods=['POST'])
def predict():
    data = {"success": False}

    gender, age, main_format, children, crazy_purchases_goods_count_6m, k_var_cheque_group_width_15d, promo_share_15d = '', None, None, None, None, None, None

    request_json = request.get_json()

    if request_json['gender']:
        gender = request_json['gender']

    if request_json['age'] is not None:
        age = request_json['age']

    if request_json['main_format'] is not None:
        main_format = request_json['main_format']

    if request_json['children'] is not None:
        children = request_json['children']

    if request_json['crazy_purchases_goods_count_6m'] is not None:
        crazy_purchases_goods_count_6m = request_json['crazy_purchases_goods_count_6m']

    if request_json['k_var_cheque_group_width_15d'] is not None:
        k_var_cheque_group_width_15d = request_json['k_var_cheque_group_width_15d']

    if request_json['promo_share_15d'] is not None:
        promo_share_15d = request_json['promo_share_15d']

    sm_predictions = pipeline.predict(pd.DataFrame({'gender': [gender],
                                                    'age': [age],
                                                    'main_format': [main_format],
                                                    'children': [children],
                                                    'crazy_purchases_goods_count_6m': [crazy_purchases_goods_count_6m],
                                                    'k_var_cheque_group_width_15d': [k_var_cheque_group_width_15d],
                                                    'promo_share_15d': [promo_share_15d]}))

    data['predictions'] = sm_predictions[0]
    data['success'] = True
    print('Ok')

    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')