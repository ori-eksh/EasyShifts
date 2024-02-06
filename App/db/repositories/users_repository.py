from sqlalchemy.orm import Session
from App.db.models import User
from App.db.repositories.base_repository import BaseRepository


class UsersRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, User)