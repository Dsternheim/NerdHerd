from google.cloud import bigquery
from google.oauth2 import service_account
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn import model_selection
import numpy as np


def run_lgr(df, x_test):
    y = df[u'hypev_hypertension__1_Yes']
    features = list(df.columns[:12]) + list(df.columns[13:])
    print(len(x_test))
    print('features:')
    print(features)
    x = df[features]
    x_train, x_test1, y_train, y_test = model_selection.train_test_split(x, y, test_size=.4, random_state=0)
    lgr = LogisticRegression()
    lgr = lgr.fit(x_train, y_train)
    scores = model_selection.cross_val_score(lgr, x, y, cv=10)
    print('Logistic Regression accuracy: ' + str(round(scores.mean() * 100, 2)) + '%')
    x_test = np.reshape(x_test, (1, -1))
    y_pred = lgr.predict(x_test)
    print(int(y_pred))
    return int(y_pred)


def update_rhr():
    client.query("""
    DELETE FROM usr_data.usr_data_tbl WHERE aweightp=150
    """)
    return


credentials = service_account.Credentials.from_service_account_file(
    'NerdHerd.json')
project_id = 'nerdherd'
client = bigquery.Client(credentials=credentials, project=project_id)

df = client.query("""
  SELECT *
  FROM ml_health_data.health_data_tbl
""").to_dataframe()
# print(df.head())
# cols = list(df.columns)
# print(cols)
# x_test = [2,70,150,1,0, 1,0,1,0,0,0, 0, 0,0,1, 0,1, 0,1, 0,1, 1,0, 0,1,0, 0,1, 1,0,0,0,0, 1,0,0,0,0, 1,0,0,0,0, 0,0,1, 1,0,0,0,0,0, 0,0,0,1, 0,0, 53]
# hypertension_value = run_lgr(df, x_test)
# print('Hypertension' + str(hypertension_value))


