import pandas as pd

class checkdataquality:
    def __init__(self, path):
        self.path = path
        self.df = None

    def load(self):
        self.df = pd.read_csv(self.path, sep='|', low_memory=False)
        return self.df

    def show_info(self):
        if self.df is not None:
            print(self.df.info())
            print(self.df.describe())
        else:
            print("Data not loaded yet. Please call the load method first.")

    def missing_summary(self):
        if self.df is not None:
            missing_counts = self.df.isnull().sum()
            print("Missing values per column:")
            print(missing_counts)
        else:
            print("Data not loaded yet. Please call the load method first.")
