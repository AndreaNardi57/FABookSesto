from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date


class BookBase(BaseModel):
    operazione: str
    dataRitiro: date
    dataChiusura: date | None = None
    autore: str
    titolo: str
    
    @field_validator("dataChiusura", mode="before")
    def empty_string_to_none(cls, v):
        if v == "" or v is None:
            return None
        return v
    
class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "user"

class UserResponse(BaseModel):
    id: int
    username: str
    role: str
    fname: str
    lname: str
    email_address: str
