from fastapi import APIRouter

from ..models import User


router = APIRouter(prefix='/users')


@router.get('/', response_model=list[User])
async def get_users() -> User:
    """Return `User` model."""

    return User()
