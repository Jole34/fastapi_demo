import traceback
from typing import Dict, Optional
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from config.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models import User
from schemas import UserCreate


class CRUDUser(CRUDBase[User, UserCreate, Dict]):

    def create_user(self, db: Session, obj_in: UserCreate, **kwargs) -> User:
        db_us = User(
            name=obj_in.name,
            email=obj_in.email.lower(),
            hashed_password=get_password_hash(obj_in.password)
        )

        db.add(db_us)
        try:
            db.commit()
        except SQLAlchemyError:
            traceback.print_exc()
            return None
        return db_us


    def authenticate(self, db: Session, email: str, password: str, **kwargs) -> Optional[User]:
        us = self.get_by_email(db, email=email)
        if not us:
            return None
        if not verify_password(password, us.hashed_password):
            return None
        return us

    def get_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()


user = CRUDUser(User)
