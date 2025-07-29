from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import UserCreate, UserOut
from app.services.user_service import create_user
from app.db.session import get_session

router = APIRouter()

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    try:
        created_user = await create_user(user, session)
        return created_user
    except IntegrityError:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": "User with this email already exists."})
