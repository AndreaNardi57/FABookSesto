from sqlalchemy import Column, Integer, String, Date, Boolean, Float,TIMESTAMP
from database import Base
from sqlalchemy.sql import func

class Book(Base):
    __tablename__ = "storico"

    id = Column(Integer, primary_key=True, index=True)
    operazione = Column(String)
    dataRitiro = Column(String)
    dataChiusura = Column(String)
    autore = Column(String)
    titolo = Column(String, index=True)
    
    
# Create the database tables
from database import engine
Base.metadata.create_all(bind=engine)
