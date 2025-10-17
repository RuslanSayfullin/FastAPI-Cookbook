from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_engine, Base, get_db_session
from operations import create_ticket


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
    await engine.dispose()

app = FastAPI(
    title="SettingUpSQLAlchemy",
    description="SettingUpSQLAlchemy",
    version="0.0.1",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*"
)

class TicketRequest(BaseModel):
    price: float | None
    show: str | None
    user: str | None = None

@app.post("/ticket", response_model=dict[str, int])
async def create_ticket_route(
    ticket: TicketRequest, 
    db_session: Annotated[AsyncSession, Depends(get_db_session)]
):
    ticket_id = await create_ticket(
        db_session,
        ticket.show,
        ticket.user,
        ticket.price,
    )
    return {"ticket_id": ticket_id}
