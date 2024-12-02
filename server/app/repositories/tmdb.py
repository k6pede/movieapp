import json
import requests
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
   tmdb_api_key: str
   tmdb_api_access_token: str
   tmdb_base_url: str
   tmdb_img_url: str
   class Config:
      env_file = ".env"

settings = Settings()

class TmdbRepository :
  def __init__(self) -> None:
   self.token = settings.tmdb_api_access_token
   self.headers_ = {"accept": "application/json","Authorization": f"Bearer {self.token}",  'Content-Type': 'application/json;charset=utf-8'}
   self.base_url_ = settings.tmdb_base_url
   self.img_url = settings.tmdb_img_url

  # _から始まるメソッドはこのクラス内で内部的にのみ使用するもの。慣例。
  def _json_by_get_request(self, url, params={}):
   # paramsはクエリパラメータ
   response = requests.get(url, headers=self.headers_, params=params)
   return json.loads(response.text)

# languageをフロント側でリクエストに含め、指定できるようにする
# Pythondではメソッド名はスネークケース get_movie_by_idでよくね？
  def search_movies(self, query):
   params = {'query': query}
   url = f'{self.base_url_}search/movie'
   return self._json_by_get_request(url, params)

  def get_movie_images(self, movie_id):
   """
   映画のスチル写真を取得する
   """
   url = f'{self.base_url_}movie/{movie_id}/images'
   return self._json_by_get_request(url)

  def get_popular_movies(self, language=None, region=None):
   """
   今話題の映画を取得する
   """
   url = f'{self.base_url_}movie/popular'
   return self._json_by_get_request(url)


# 　TODO:名前付き引数はどのように設定しているかを確認する.
  def get_top_rated_movies(self,  page:int, language:str):
   """
   movie
   1ページあたり20件の映画情報を取得する
   """
   url = f'{self.base_url_}movie/top_rated?api_key={settings.tmdb_api_key}&page={page}&language={language}'
   response = requests.get(url)
   data = response.json()
   print(data)
   return data
