# src/check_data_quality.py

import pandas as pd

class checkdataquality:
    def __init__(self, path):
        self.path = path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.path, sep='|', low_memory=False)
        return self.df

    def basic_info(self):
        if self.df is not None:
            print(self.df.info())
            print(self.df.describe())
        else:
            print("Data not loaded yet. Please call the load_data method first.")
