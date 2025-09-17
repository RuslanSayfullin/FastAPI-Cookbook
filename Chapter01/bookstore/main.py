from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 


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