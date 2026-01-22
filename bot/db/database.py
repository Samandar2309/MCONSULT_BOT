from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from config import DATABASE_URL


# =====================================================
# 🔹 SQLALCHEMY BASE
# =====================================================
class Base(DeclarativeBase):
    pass


# =====================================================
# 🔹 ASYNC ENGINE
# =====================================================
engine = create_async_engine(
    DATABASE_URL,
    echo=True,          # productionda False qilamiz
    future=True,
)


# =====================================================
# 🔹 SESSION FACTORY
# =====================================================
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# =====================================================
# 🔹 SESSION DEPENDENCY
# =====================================================
async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
