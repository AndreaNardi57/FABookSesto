from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import engine, get_db

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Library Management API")

# Books CRUD Endpoints
@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    # Check if book with same ISBN already exists
    db_book = crud.get_book_by_isbn(db, isbn=book.isbn)
    if db_book:
        raise HTTPException(status_code=400, detail="Book with this ISBN already exists")
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@app.get("/books/{isbn}", response_model=schemas.Book)
def read_book(isbn: str, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_isbn(db, isbn=isbn)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.put("/books/{isbn}", response_model=schemas.Book)
def update_book(isbn: str, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db, isbn=isbn, book_update=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.delete("/books/{isbn}")
def delete_book(isbn: str, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, isbn=isbn)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": "Book deleted successfully"}

# Running the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
