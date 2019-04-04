import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
from scipy.stats import truncnorm
from pandas import ExcelWriter

def main():
    df = pd.read_excel('2012 final.xlsx')  # reading in the data
    print(df.head())
    df = pd.get_dummies(df)  # converting categorial variables to dummy columns
    print(df.head())
    print(df.columns)
    df = df[df.columns.drop(list(df.filter(regex='Don\'t know')))]  # Dropping don't know columns
    df = df[df.columns.drop(list(df.filter(regex='Not ascertained')))]  # Dropping not ascertained columns
    df = df[df.columns.drop(list(df.filter(regex='Not mentioned')))]  # Dropping not mentioned columns
    print(df.columns)
    # lower, upper, mu, and sigma are four parameters
    lower, upper = 40, 130
    mu, sigma = 62.5, 30
    # instantiate an object X using the above four parameters,
    X = truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)

    # generate 34000 sample data
    samples = X.rvs(34300)
    df['rhr'] = pd.Series(samples.astype(int))
    df_nan = Imputer(missing_values=np.nan, strategy='most_frequent', axis=1)  # Imputing most frequent values for NaN
    df_imp = pd.DataFrame(df_nan.fit_transform(df))  # Executes the Imputer
    df_imp.columns = df.columns  # Restores columns
    df_imp.index = df.index  # Restores indexes
    print(df_imp.head())
    writer = ExcelWriter('mlhealthdata.xlsx', engine='xlsxwriter')  # selecting excel sheet to be written
    df_imp.to_excel(writer, 'Sheet1')  # choosing what dataframe to save
    writer.save()  # saving data to the specified excel sheet


if __name__ == '__main__':
    main()

