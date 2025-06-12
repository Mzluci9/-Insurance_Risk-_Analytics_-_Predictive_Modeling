import pandas as pd

class DataCleaner:
    def __init__(self, df):
        self.df = df
    
    def clean_missing(self):
        # Remove columns with more than 50% missing values
        limit = len(self.df) * 0.5
        cleaned_df = self.df.dropna(thresh=limit, axis=1).copy()
        
        # Fill missing numerical values with median, categorical with mode
        for col in cleaned_df.columns:
            if cleaned_df[col].dtype == 'object':
                mode_val = cleaned_df[col].mode()[0]
                cleaned_df.loc[:, col] = cleaned_df.loc[:, col].fillna(mode_val)
            else:
                median_val = cleaned_df[col].median()
                cleaned_df.loc[:, col] = cleaned_df.loc[:, col].fillna(median_val)
        
        self.df = cleaned_df
        return cleaned_df
    
    def no_missing(self):
        return self.df.isnull().sum().sum() == 0
