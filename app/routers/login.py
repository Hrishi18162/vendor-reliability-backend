
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, crud
from app.auth import verify_password, create_access_token

router = APIRouter(
    prefix="/users",
    tags=["Login"]
)


@router.post("/login")
def login(
    user: schemas.UserLogin,
    db: Session = Depends(get_db)
):
    db_user = crud.get_user_by_email(
        db,
        user.email
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    print("Entered Email:", user.email)
    print("Entered Password:", user.password)
    print("Stored Hash:", db_user.password)

    password_valid = verify_password(
        user.password,
        db_user.password
    )

    print("Verify Result:", password_valid)

    if not password_valid:
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token({
        "email": db_user.email,
        "role": db_user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }