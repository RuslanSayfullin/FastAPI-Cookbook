from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession

class Base(DeclarativeBase):
    pass

class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column(nullable=True)
    show: Mapped[str | None]
    user: Mapped[str | None]

DATABASE_URL = (
    "sqlite+aiosqlite:///.database.db"
)

def get_engine() -> AsyncEngine:
    return create_async_engine(
        DATABASE_URL, echo=True
    )


AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=get_engine(),
    class_=AsyncSession
)


async def get_db_session():
    async with AsyncSessionLocal() as session:
        yield session