from sklearn.metrics.pairwise import cosine_similarity
    
    
class TopByOverview():
    def __init__(self, model2, df):
        self.model2 = model2     
        self.df = df   
        
    def TopByOverview(self, title: str, n_recommendations: int = 10):
        
        if title not in self.df['Title'].values:
            raise ValueError(f"Title '{title}' not found in dataset.")
        
        idx = self.df[self.df['Title'] == title].index[0]

        cosine_sim = cosine_similarity(self.model2[idx], self.model2)

        sim_scores = list(enumerate(cosine_sim[0]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        movie_indices = [i[0] for i in sim_scores[1:n_recommendations + 1]]

        return [(self.df.iloc[i]['Title'], self.df.iloc[i]['Genre_Combined']) for i in movie_indices]
        
        
    
           
