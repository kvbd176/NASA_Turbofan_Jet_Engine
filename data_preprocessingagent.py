import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

class DataPreprocessingAgent:

    def __init__(self):
        self.scaler = MinMaxScaler()

    def load_data(self, train_path, test_path, rul_path):
        train = pd.read_csv(train_path, sep=r"\s+", header=None)
        test = pd.read_csv(test_path, sep=r"\s+", header=None)
        rul = pd.read_csv(rul_path, header=None)

        return train, test, rul

    def assign_columns(self, train, test):

        columns = [
            'engine_id','cycle',
            'setting1','setting2','setting3'
        ]

        for i in range(1,22):
            columns.append(f'sensor{i}')

        train.columns = columns
        test.columns = columns

        return train, test

    def validate(self, train):

        print("Shape:", train.shape)
        print("Missing:", train.isnull().sum().sum())
        print("Duplicates:", train.duplicated().sum())

    def generate_rul(self, train):

        max_cycle = train.groupby("engine_id")["cycle"].max().reset_index()

        max_cycle.columns = ["engine_id","max_cycle"]

        train = train.merge(max_cycle,on="engine_id")

        train["RUL"] = train["max_cycle"] - train["cycle"]

        train.drop("max_cycle",axis=1,inplace=True)

        return train

    def remove_constant_features(self, train, test):

        drop_cols = [
            "setting3",
            "sensor1",
            "sensor5",
            "sensor16",
            "sensor18",
            "sensor19"
        ]

        train.drop(columns=drop_cols,inplace=True)
        test.drop(columns=drop_cols,inplace=True)

        return train, test

    def normalize(self, train, test):

        feature_cols = train.columns.difference(
            ["engine_id","cycle","RUL"]
        )

        train[feature_cols] = self.scaler.fit_transform(train[feature_cols])

        test[feature_cols] = self.scaler.transform(test[feature_cols])

        joblib.dump(self.scaler,"scaler.pkl")

        return train,test

    def preprocess(self, train_path, test_path, rul_path):

        train,test,rul = self.load_data(
            train_path,
            test_path,
            rul_path
        )

        train,test = self.assign_columns(train,test)

        self.validate(train)

        train = self.generate_rul(train)

        train,test = self.remove_constant_features(train,test)

        train,test = self.normalize(train,test)

        train["RUL"] = train["RUL"].clip(upper=125)

        return train,test,rul
