from fastapi import (
    Depends,
    HTTPException
)

from fastapi.security import OAuth2PasswordBearer

from jose import jwt

from dotenv import load_dotenv

import os

from database.database import SessionLocal
from database.models import User


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = "HS256"


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        db = SessionLocal()

        try:

            user = db.query(User).filter(
                User.id == int(user_id)
            ).first()

            if user is None:

                raise HTTPException(
                    status_code=401,
                    detail="User not found"
                )

            return user

        finally:

            db.close()

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )