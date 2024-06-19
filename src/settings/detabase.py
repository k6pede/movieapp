# pythonアプリからsqlalchemyを使ってdbに接続するための処理

from src.settings.env import Env
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.engine import URL  # type: ignore
from sqlalchemy.orm import declarative_base, sessionmaker  # type: ignore

# db接続用のURLの構築
_database_url = URL.create(
    drivername="mysql-mysqldb",
    username=Env.DB_USER,
    password=Env.DB_PASSWORD,
    host=Env.DB_HOST,
    port=Env.DB_PORT,
    database=Env.DB_NAME,
)
# エンジンの作成。このエンジンはDBとの接続を管理する心臓部
Engine = create_engine(_database_url, echo=True)

# セッションファクトリの作成。DB操作を行うためのセッションを作成する。
# sutocommit : 明示的にcommitするまでDBに反映するか
# autoflush : 各クエリが実行される前に自動的に変更をDBにflushするかどうか
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=Engine)

# ベースクラスの作成。このベースクラスがモデルクラスの基礎になる。
Base = declarative_base()


# データベースセッションを作成し、最後にはクローズする依存関係の定義
# 自動で閉じないセッションはリソースリークを引き起こす恐れがある。(使用したメモリが解放されず無駄に保持され続ける状況)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
