FROM python:3.11

WORKDIR /server

# Poetryで依存関係をインストールするために必要なファイルをコピー
COPY pyproject.toml poetry.lock /server/

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

# 依存関係をインストールした後にサーバーコードをコピー
COPY server /server

CMD ["poetry", "run", "uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
