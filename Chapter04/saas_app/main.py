from contextlib import asynccontextmanager

from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session

from db_connection import get_engine, get_session
from models import Base
from responses import (
    UserCreateResponse,
    UserCreateBody,
    ResponseCreateUser
)
from operations import add_user
import security


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=get_engine)
    yield

app = FastAPI(
    title="Saas application", lifespam=lifespan
)

app.include_router(security.router)

@app.post(
    "/register/user",
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseCreateUser,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "The user already exists"
        }
    },
)
def register(
    user: UserCreateBody,
    session: Session = Depends(get_session),
) -> dict[str, UserCreateResponse]:
    user = add_user(
        session=session, **user.model_dump()
    )
    if not user:
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            "username or email already exists",
        )
    user_response = UserCreateResponse(
        username=user.username, email=user.email
    )
    return {
        "message": "user created",
        "user": user_response,
    }