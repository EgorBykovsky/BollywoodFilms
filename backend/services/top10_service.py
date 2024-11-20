class Top10Service():
    def __init__(self, df_top):
        self.df_top = df_top
    
    def get_top_10(self):
        return self.df_top.sort_values('w_score', ascending=False).head(10)['Title'].values.tolist()
        