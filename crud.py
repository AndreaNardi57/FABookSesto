from sqlalchemy.orm import Session
from models import Book, User
import schemas
import crud
from datetime import datetime
from sqlalchemy import or_
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)

def get_book_by_titolo(db: Session, query: str,search_field: str,skip: int = 0,limit: int = 1000):
    if search_field == "titolo":
        return db.query(Book).filter(Book.titolo.ilike(f"%{query}%")).order_by(Book.dataRitiro.desc()).offset(skip).limit(limit).all()
    elif search_field == "autore":
        return db.query(Book).filter(Book.autore.ilike(f"%{query}%")).order_by(Book.dataRitiro.desc()).offset(skip).limit(limit).all()

def get_books_count_filtered(db: Session, query: str):
    return db.query(Book).filter(or_(Book.titolo.ilike(f"%{query}%"),Book.autore.ilike(f"%{query}%"))).count()

def get_books(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(Book).order_by(Book.dataRitiro.desc()).offset((skip-1)*limit).limit(limit).all()

def get_books_count(db: Session):
    return db.query(Book).count()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, id: str, book_update: schemas.BookCreate):
    db_book = db.query(Book).filter(Book.id == id).first()
    if db_book:
        for key, value in book_update.dict().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, id: str):
    db_book = db.query(Book).filter(Book.id == id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

def return_book(db: Session, id: str):
    db_book = db.query(Book).filter(Book.id == id).first()
    giorno = datetime.now().date()
    if db_book:
        db_book.dataChiusura = giorno
    db.commit()
    db.refresh(db_book)
    return db_book

def get_user_by_username(db: Session, username: str):
    db_user = db.query(User).filter(User.username == username).first()
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    db_user = get_user_by_username(db, username)
    if db_user.role == 'beginner':
        return None
    if not db_user.username or not verify_password(password, user.hashed_password):
        return None
    return user

def chk_book_by_titolo(db: Session, titolo: str):
    return db.query(Book).filter(Book.titolo == titolo).first()