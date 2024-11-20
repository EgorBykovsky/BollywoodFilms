import pickle
import pandas as pd

class ModelLoader:
    def __init__(self, model_path: str, df_path: str, df_top_path: str, model_overview_path: str):
        self.model_path = model_path
        self.df_path = df_path
        self.df_top_path = df_top_path   
        self.model_overview_path = model_overview_path
        
        
    def load_model(self):
        try:
            with open(self.model_path, 'rb') as file:
                self.model = pickle.load(file)
                return self.model
        except Exception as e:
            print(f"Error loading model: {e}")
            return None

    def load_df(self):
        try:
            self.df = pd.read_csv(self.df_path, sep='\t')
            print("DataFrame loaded successfully.")
        except Exception as e:
            print(f"Error loading DataFrame: {e}")
            self.df = None
        return self.df
    
    
    def load_top_df(self):
        try:
            self.df_top = pd.read_csv(self.df_top_path, sep='\t')
            print("Top DataFrame loaded successfully.")
        except Exception as e:
            print(f"Error loading DataFrame: {e}")
            self.df_top = None
        return self.df_top
    
    def load_model_overview(self):
        try:
            with open(self.model_path, 'rb') as file:
                self.model2 = pickle.load(file)
                return self.model2
        except Exception as e:
            print(f"Error loading model: {e}")
            return None
            
    