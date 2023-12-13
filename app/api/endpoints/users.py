from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from api.deps import *
from typing import Any
from schemas import UserCreate, UserOut
from crud import user
from models import User

router = APIRouter()


@router.post('/', response_model=UserOut)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate
) -> Any:
    user_created = user.create_user(db, obj_in=user_in)
    if not user_created:
        raise HTTPException(status_code=400, detail="Korisnik nije uspesno kreiran.")
    return user_created


@router.get('/', response_model=UserOut)
def get_user_info(
    *,
    current_user: User = Depends(get_current_user_resp)
) -> Any:
    """

    :param current_user:
    :return:

    Return logged user information

    """
    return current_user

