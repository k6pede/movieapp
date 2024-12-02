import time
from fastapi import FastAPI

# ここで呼び出しているFastAPIのアプリケーションインスタンスと、main.pyのインスタンスは異なるのか？
# AI曰くYES 複数のインスタンスを異なるファイルで生成するのではなく、主要なエントリポイントで一つのインスタンスを生成し、
# そのインスタンスにルーターやミドルウェアを登録していく設計が一般的
app = FastAPI()

@app.middleware("http")
async def add_process_time_header():
    print('======通った=====')
