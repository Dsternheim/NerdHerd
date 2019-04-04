from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn import model_selection
import numpy as np


def main():
    df = pd.read_excel('mlhealthdata.xlsx')
    y = df['hypev(hypertension)_1 Yes']
    features = list(df.columns[:12]) + list(df.columns[13:])
    x = df[features]
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=.4, random_state=0)
    lgr = LogisticRegression()
    lgr = lgr.fit(x_train, y_train)
    scores = model_selection.cross_val_score(lgr, x, y, cv=10)
    print('Logistic Regression accuracy: ' + str(round(scores.mean() * 100, 2)) + '%')
    x_test = [2,70,150,1,0, 1,0,1,0,0,0, 0, 0,0,1, 0,1, 0,1, 0,1, 1,0, 0,1,0, 0,1, 1,0,0,0,0, 1,0,0,0,0, 1,0,0,0,0, 0,0,1, 1,0,0,0,0,0, 0,0,0,1, 0,0, 53]
    x_test = np.reshape(x_test, (1, -1))
    y_pred = lgr.predict(x_test)
    print(y_pred)


if __name__ == '__main__':
    main()
