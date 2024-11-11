import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data loader and preprocessing class
class NBADataLoader:
    def __init__(self, file_path, encoding='ISO-8859-1', delimiter=';'):
        self.file_path = file_path
        self.encoding = encoding
        self.delimiter = delimiter
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path, encoding=self.encoding, delimiter=self.delimiter)
        print("Data loaded successfully.")
        return self.data

    def check_nulls_and_dtypes(self):
        print("Data types:\n", self.data.dtypes)
        print("\nNull values:\n", self.data.isnull().sum())

    def fill_missing_values(self, percentage_columns):
        self.data[percentage_columns] = self.data[percentage_columns].fillna(0)
        self.data[percentage_columns] = self.data[percentage_columns].astype(float)
        print("Missing values filled in percentage columns.")
        return self.data

    def add_rpg_column(self):
        self.data['RPG'] = self.data['ORB'] + self.data['DRB']
        print("Rebounds per Game (RPG) column added.")
        return self.data
