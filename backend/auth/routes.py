from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database.database import get_db
from database.models import User
from database.schemas import (
    UserCreate,
    UserLogin,
    UserResponse
)

from auth.security import (
    hash_password,
    verify_password
)

from auth.jwt import (
    create_access_token
)
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)



# REGISTER

@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user:UserCreate,
    db:Session=Depends(get_db)
):


    existing_user = db.query(User).filter(
        User.email==user.email
    ).first()


    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )


    new_user=User(

        username=user.username,

        email=user.email,

        hashed_password=hash_password(
            user.password
        )

    )


    db.add(new_user)

    db.commit()

    db.refresh(new_user)


    return new_user





# LOGIN

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        form_data.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": str(db_user.id),
            "email": db_user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }