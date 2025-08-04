from fastapi import FastAPI
from pydantic import BaseModel
from RedditScraperDAO import getDiscussionsAsync

app = FastAPI()
    
    
@app.get("/reddit-posts")
async def redditPosts():
    discussions = await getDiscussionsAsync()
    print(discussions)
