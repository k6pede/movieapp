from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.handlers import sample, movie
from starlette.middleware.base import BaseHTTPMiddleware


app = FastAPI(docs_url="/docs")

app.include_router(sample.router)
app.include_router(movie.router)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# これは通る settings.middleware.pyに書いても通らない．．．なぜ？
# @app.middleware("http")
class CustomMiddleware(BaseHTTPMiddleware):
    # BaseHTTPMiddlewareを継承したクラス内でdispatchをオーバーライドした場合、クラスのインスタンスメソッドになるため、第一引数はselfが必要
    async def dispatch(self, request, call_next):
        print("##### Middleware-1 Start #####")
        response = await call_next(request)
        print("##### Middleware-1 Finish #####")

        return response


app.add_middleware(CustomMiddleware)
