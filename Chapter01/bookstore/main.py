from starlette.responses import JSONResponse
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel

from models import Book


app = FastAPI(title="First application",
            description="My first application on FastAPI",
            version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class BookResponse(BaseModel):
    title: str
    author: str

@app.get("/allbooks")
async def read_all_books() -> list[BookResponse]:
    return [
        {
            "id": 1,
            "title": "1984",
            "author": "George Orwell",
        },
        {
            "id": 2,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
        }
    ]


@app.get("/book/{book_id}")
async def read_book(book_id: int):
    return {
        "book_id": book_id,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    }

@app.get("/books")
async def read_books(year: int = None):
    if year:
        return {
            "year": year,
            "books": ["Book 1", "Book 2"]
        }                     
    return {"books": ["All Books"]}

@app.get("/authors/{author_id}")
async def reaad_author(author_id: int):
    return {
        "author_id": author_id,
        "name": "Ernest Hemingway"
    }

@app.post("/book")
async def create_bool(book: Book):
    return book

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": "Oops! Something went wrong"
        }
    )

@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)
