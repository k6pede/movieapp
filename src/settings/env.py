import os

import dotenv  # type: ignore

dotenv.load_dotenv(dotenv.find_dotenv())


def _get_env(key: str):
    env = os.getenv(key)
    if env is None:
        return env

    if env.strip() == "":
        os.environ.pop(key)
        return None

    return env


def _get_env_or_default(key: str, default: str):
    env = _get_env(key)
    if env is None:
        return default
    return env


class Env:
    # tmdb関係
    TMDB_API_KEY = _get_env("TMDB_API_KEY")
    TMDB_API_ACCESS_TOKEN = _get_env("TMDB_API_ACCESS_TOKEN")
    TMDB_BASE_URL = _get_env("TMDB_BASE_URL")
    TMDB_IMG_URL = _get_env("TMDB_IMG_URL")

    # db関係
    DB_USER = _get_env("DB_USER")
    DB_PASSWORD = _get_env("DB_PASSWORD")
    DB_HOST = _get_env("DB_HOST")
    DB_PORT = _get_env("DB_PORT")
    DB_NAME = _get_env("DB_NAME")
