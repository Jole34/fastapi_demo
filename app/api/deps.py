from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

import crud
from models import User
import schemas
from config.setup import settings
from db.session import SessionLocal
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/api/login/access-token"
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> any:
    try:
        payload = jwt.decode(
            token, settings.KEY, algorithms=["HS256"]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.user.get(db=db,id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="Korisnik nije pronađen.")
    return user


def get_current_user_resp(
    current_sp: User = Depends(get_current_user),
) -> any:
    return current_sp


