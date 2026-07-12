from fastapi import APIRouter, HTTPException
from database.db import SessionLocal
from database.models import Favorite

router = APIRouter()


@router.post("/add")
def add_favorite(data: dict):

    db = SessionLocal()

    fav = Favorite(
        user_id=data["user_id"],
        recipe_name=data["recipe_name"],
        recipe_image=data["recipe_image"],
        youtube=data["youtube"]
    )

    db.add(fav)

    db.commit()

    return {
        "success": True
    }


@router.get("/{user_id}")
def get_favorites(user_id: int):

    db = SessionLocal()

    favorites = db.query(Favorite).filter(
        Favorite.user_id == user_id
    ).all()

    return favorites


@router.delete("/{favorite_id}")
def remove_favorite(favorite_id: int):

    db = SessionLocal()

    fav = db.query(Favorite).filter(
        Favorite.id == favorite_id
    ).first()

    if not fav:

        raise HTTPException(
            status_code=404,
            detail="Favorite not found"
        )

    db.delete(fav)

    db.commit()

    return {
        "success": True
    }