import pandas as pd
from sklearn.feature_selection import SelectKBest


def clean_dataset():
    # Load in the dataset
    data = pd.read_csv('./Data/initial_dataset.csv')

    # Drop unnecessary columns
    data = data.drop(['TAIL_NUM', 'OP_UNIQUE_CARRIER'], axis=1)

    # Fix datatype
    data['Dew Point'] = data['Dew Point'].astype(int)

    # Target variable
    X = data.drop('TAXI_OUT', axis=1)
    y = data['TAXI_OUT']
    


    # One hot encode with pandas
    #encoded_data = pd.get_dummies(data, columns=['Wind', 'Condition', 'DEST'])

    print(data.dtypes)


clean_dataset()
