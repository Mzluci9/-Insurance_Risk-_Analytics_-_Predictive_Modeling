class cleandataprocessing:
    def __init__(self, df):
        self.df = df

    def clean_missing_values(self):
        limit = len(self.df) * 0.5
        cleaned_df = self.df.dropna(thresh=limit, axis=1).copy()

        for col in cleaned_df.columns:
            if cleaned_df[col].dtype == 'object':
                mode_val = cleaned_df[col].mode()[0]
                cleaned_df[col] = cleaned_df[col].fillna(mode_val)
            else:
                median_val = cleaned_df[col].median()
                cleaned_df[col] = cleaned_df[col].fillna(median_val)

        self.df = cleaned_df
        return cleaned_df

    def verify_no_missing_values(self):
        return self.df.isnull().sum().sum() == 0
