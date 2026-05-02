from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from config import DATABASE_URL



engine = create_async_engine(
    DATABASE_URL,
    echo=False,          # PROD da False
    pool_pre_ping=True,  # uzilgan connectionni tekshiradi
    future=True,
)


async_session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
