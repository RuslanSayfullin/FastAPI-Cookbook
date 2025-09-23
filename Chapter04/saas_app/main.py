from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from db_connection import get_engine, get_session
from models import Base
from operations import add_user
from responses import ResponseCreateUser, UserCreateBody, UserCreateResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=get_engine())
    yield

app = FastAPI(title="Chapter04",
        description="Authentication and Authorization",
        version="0.0.1", 
        lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_crdentials=True,
    allow_methods="*",
    allow_headers="*"
)

@app.post("/register/user", status_code=status.HTTP_201_CREATED,
    response_model=ResponseCreateUser,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "The user already exists"
        }
    },
)
def register(user: UserCreateBody,
    session: Session = Depends(get_session),) -> dict[str, UserCreateResponse]:
    user = add_user(session=session, **user.model_dump())

    if not user:
        raise HTTPException(status.HTTP_409_CONFLICT, "username or mail already exists")
    
    user_response = UserCreateResponse(username=user.username, email=user.email)

    return {
        "message": "user created",
        "user": user_response
    }