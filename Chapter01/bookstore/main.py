import json
from typing import Dict

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.responses import JSONResponse
from pydantic import BaseModel

from models import Book

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": "Oops! Something went wrong"
        },
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return PlainTextResponse(
        "This is a plain text response:"
        f" \n{json.dumps(exc.errors(), indent=2)}",
        status_code=status.HTTP_400_BAD_REQUEST,
    )

@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)

@app.get("/books")
async def read_books(year: int = None) -> Dict:
    if year:
        return {
            "year": year,
            "books": ["Book1", "Book2"]
        }
    return {"books": ["All Books"]}

@app.get("/books/{book_id}")
async def read_book(book_id: int) -> Dict:
    return {
        "book_id": book_id,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    }

@app.get("/authors/{author_id}")
async def read_author(author_id: int):
    return {
        "author_id": author_id,
        "name": "Ernest Hemingway"
    }

class BookResponse(BaseModel):
    title: str
    author: str

@app.get("/allbooks")
async def read_all_books() -> list[BookResponse]:
    return [
        {
            "id": 0,
            "title": "1984",
            "author": "George Orwell"
        },
        {
            "id": 1,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
        }
    ]

@app.post("/book")
async def create_book(book: Book):
    return book

