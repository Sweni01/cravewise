from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from database.db import SessionLocal
from database.models import User

from services.auth_service import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()


@router.post("/signup")
def signup(user: dict):

    db: Session = SessionLocal()

    existing = db.query(User).filter(
        User.email == user["email"]
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        username=user["username"],
        email=user["email"],
        password=hash_password(user["password"])
    )

    db.add(new_user)
    db.commit()

    return {
        "success": True,
        "message": "Account created successfully"
    }
@router.post("/login")
def login(user: dict):

    db = SessionLocal()

    existing = db.query(User).filter(
        User.email == user["email"]
    ).first()

    if not existing:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        user["password"],
        existing.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        {
            "user_id": existing.id,
            "email": existing.email
        }
    )

    return {
        "success": True,
        "access_token": token,
        "token_type": "bearer"
    }