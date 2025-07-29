from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import UserCreate
from app.db.tables import User

async def create_user(user_data: UserCreate, session: AsyncSession):
    new_user = User(email=user_data.email, password=user_data.password)
    session.add(new_user)
    try:
        await session.commit()
        await session.refresh(new_user)
    except IntegrityError:
        await session.rollback()
        raise
    return new_user
