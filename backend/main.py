from fastapi import FastAPI, Depends, Query, HTTPException
from recomendation_model import ModelLoader
from services.top10_service import Top10Service
from services.top10_by_genre import TopByGenre
from services.top10_overview import TopByOverview
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader = ModelLoader(model_path='tfidf_matrix.pkl', df_path="df.csv", df_top_path='top.csv', model_overview_path='tfidf_matrix2.pkl')
model = model_loader.load_model()
df = model_loader.load_df()
df_top = model_loader.load_top_df()
model2 = model_loader.load_model_overview()

if model is None:
    raise RuntimeError("Failed to load the recommendation model.")

if df is None:
    raise RuntimeError("Failed to load the df.")


def get_top10_genre_service():
    return TopByGenre(model, df)

def get_top():
    return Top10Service(df_top)

def get_top_overview():
    return TopByOverview(model2, df)

class RecommendationRequest(BaseModel):
    title: str

@app.post("/top10_genres")
async def top10_genres(
    request: RecommendationRequest,
    service: TopByGenre = Depends(get_top10_genre_service)
):
    try:
        top_10 = service.get_top_10(title=request.title)
        return {"top_10_genres": top_10}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    

@app.post("/top10")
async def top10(   
    service: Top10Service = Depends(get_top)
):
    try:
        top_10 = service.get_top_10()
        return {"top_10": top_10}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    

@app.post("/top10_overview")
async def top10_overview(   
    request: RecommendationRequest,
    service: TopByOverview = Depends(get_top_overview)
):
    try:
        top_10_overview = service.TopByOverview(title=request.title)
        return {"top_10_overview": top_10_overview}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))