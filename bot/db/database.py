from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from config import DATABASE_URL



class Base(DeclarativeBase):
    pass



engine = create_async_engine(
    DATABASE_URL,
    echo=True,          
    future=True,
)



AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)



async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
