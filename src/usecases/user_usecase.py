from abc import ABCMeta, abstractmethod
from sqlalchemy.orm import Session
from fastapi import Request


class User:
    id: str
    name: str
    email: str


class UserUseCase(metaClass=ABCMeta):
    def __init__(self):
        self.name = "jj"

    @abstractmethod
    def auth_uesr(self, db: Session, request: Request) -> User:
        raise NotImplementedError()
