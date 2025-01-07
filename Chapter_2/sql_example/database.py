from sqlalchemy import (
    create_engine,
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

class User(Base):
    _tablename__ = "user"
    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    name: Mapped[str]
    email: Mapped[str]


Base.metadata.create_all(bind=engine)