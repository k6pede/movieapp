from fastapi import FastAPI
from .routers import sample, movie

app = FastAPI(docs_url="/docs")

app.include_router(sample.router)
app.include_router(movie.router)