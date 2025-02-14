import json
from fastapi import APIRouter, Depends, HTTPException, Request
import requests
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from typing import Annotated, Optional

from server.app.repositories.tmdb import TmdbRepository


class MovieRequest(BaseModel):
    movie_id: int


class Settings(BaseSettings):
    tmdb_api_key: str
    tmdb_api_access_token: str
    tmdb_base_url: str

    class Config:
        env_file = ".env"


# 環境変数群
settings = Settings()
api_key = settings.tmdb_api_key
api_access_token = settings.tmdb_api_access_token
tmdb_base_url = settings.tmdb_base_url
headers = {"accept": "application/json", "Authorization": f"Bearer {api_access_token}"}

# TMDB API公式リファレンス
# https://developer.themoviedb.org/reference/intro/getting-started
router = APIRouter()

language = "ja-JA"


# TODO:422エラーの詳細が出力されないため、エラーハンドリングを行う

# TODO: 定数にまとめる
MIN_PAGE = 1
MAX_PAGE = 500


@router.get("/movie/top/{page}", summary="人気top10の映画情報取得")
def get_top_rated_movie(
    tmdb_repo: Annotated[TmdbRepository, Depends(TmdbRepository)],
    page: int = 1,
    language: str = language,
):
    """
    movie

    映画情報を人気(vote_average)順に10件取得します
    """
    # pageは1から500まで 400 Bad Requestが適切
    if page <= MIN_PAGE | page > MAX_PAGE:
        raise HTTPException(
            status_code=400, detail=f"Page must between {MIN_PAGE} and {MAX_PAGE}"
        )

    # TMDb APIから映画のリストを取得するためのURL（&language=en-US）
    # TODO:日本語英語を切り替えられるようにする
    response = tmdb_repo.get_top_rated_movies(page, language)
    return response


@router.get("/movie/popular")
def get_popular_movies(tmdb_repo: Annotated[TmdbRepository, Depends(TmdbRepository)]):
    response = tmdb_repo.get_popular_movies()
    return response


@router.get("/movie/{movie_id}", summary="映画情報取得")
def get_movie_by_id(movie_id: int):
    """
    movie

    指定したidの映画情報をTMDbから取得します
    お気に入りした映画ピンポイントの取得用
    """
    url = f"{tmdb_base_url}/movie/{movie_id}?api_key={api_key}&language={language}"
    response = requests.get(url)

    data = response.json()

    print(data)
    return {"info": data}


@router.get("/search/movie/{query}", summary="映画のタイトルで取得")
def search_movies(
    tmdb_repo: Annotated[TmdbRepository, Depends(TmdbRepository)], query: str
):
    print(query)
    response = tmdb_repo.search_movies(query)
    # data = response.json()

    return {"info": response}


@router.get("/movie/{movie_id}/images", summary="画像の取得")
def search_movies(
    # request: Request,
    tmdb_repo: Annotated[TmdbRepository, Depends(TmdbRepository)],
    movie_id: int,
):
    # query = request.path_params['query']
    response = tmdb_repo.get_movie_images(movie_id)
    return response
