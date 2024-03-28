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

class Tmdb :
  def __init__(self) -> None:
    self.token = settings.token
    self.headers_ = {"accept": "application/json","Authorization": f"Bearer {settings.token}",  'Content-Type': 'application/json;charset=utf-8'}
    self.base_url_ = settings.tmdb_base_url
    self.img_url = settings.tmdb_img_url

  
  def _json_by_get_request(self, url, params={}):
     response = requests.get(url, headers=self.headers_, params=params)
     return json.loads(response.text)
