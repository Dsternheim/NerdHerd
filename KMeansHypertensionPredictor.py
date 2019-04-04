import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from pandas import ExcelWriter

def main():
    df = pd.read_excel('mlhealthdata.xlsx')  # reading in the data
    columns = []
    for column in df:
        columns.append(column)  # making the list of columns
    df_stnd = stats.zscore(df[columns])  # standardizing the values

    model = KMeans(n_clusters=5).fit(df_stnd)  # running KMeans for 3 clusters
    labels = model.labels_  # assigning clusters
    df['clusters'] = labels
    columns.extend(['clusters'])

    print(df[columns].groupby(['clusters']).mean())  # printing stats for each cluster

    sns.lmplot('rhr', 'aweightp',
               data=df,
               fit_reg=False,
               hue="clusters",
               legend=False
               )  # plotting the KMeans

    plt.title('Clusters Hypertension vs Avg RHR')
    plt.xlabel('Hypertension')
    plt.ylabel('Avg RHR')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()


if __name__ == '__main__':
    main()


