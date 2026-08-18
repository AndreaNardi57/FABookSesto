from sqlalchemy import Column, Integer, String, Date, Boolean, Float,TIMESTAMP
from database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func

# Date_Value = 'curdate()'
Date_Value = 'CURRENT_DATE'

class Book(Base):
    __tablename__ = "storico"
    __table_args__ = {"schema": "biblio"}

    id = Column(Integer, primary_key=True, index=True)
    operazione = Column(String, nullable=False)
    dataRitiro = Column(Date, server_default=text(Date_Value))
    dataChiusura = Column(Date, nullable=True)
    autore = Column(String, nullable=False)
    titolo = Column(String, nullable=False)
    
class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "biblio"}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user", nullable=False)
    fname = Column(String, nullable=True)
    lname = Column(String, nullable=True)
    email_address = Column(String, nullable=True)

# Create the database tables
from database import engine
Base.metadata.create_all(bind=engine)
