from fastapi import APIRouter
import requests
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class MovieRequest(BaseModel):
    movie_id : int

class Settings(BaseSettings):
    api_key: str
    api_access_token: str
    
    class Config:
        env_file = ".env"

# TODO:envファイルからトークンとapiキーを取得して使う
settings = Settings()
api_key = settings.api_key
api_access_token = settings.api_access_token
print(api_key)
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_access_token}"
}

router = APIRouter()

#TODO: urlの共通部分を抜き出す


@router.get('/movie/top', summary="人気top10の映画情報取得")
def getMovieTop10():
    """
    movie

    映画情報を人気(vote_average)順に10件取得します
    """
    # TMDb APIから映画のリストを取得するためのURL（&language=en-US）
    url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url, headers)

    data = response.json()

    print(data)
    return {"info": data}

@router.get('/movie/{movie_id}', summary="映画情報取得")
def getMovieById(movie_id: int ):
    """
    movie

    指定したidの映画情報をTMDbから取得します
    お気に入りした映画ピンポイントの取得用
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)

    data = response.json()

    print(data)
    return {"info": data}

