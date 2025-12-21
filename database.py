from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

# SQLite database URL
# SQLALCHEMY_DATABASE_URL = "sqlite:////home/nardia/Lavoro/Andrea/BloccoAppunti/Python/database/BiblioSesto.db"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./BiblioSesto.db"

# MySQL database URL

SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username="biblio",
    password="biblio@1",  # Raw password
    host="localhost",
    database="bibliosesto"
 )

PG_DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username="biblio",
    password="biblio@1",
    host="localhost",
    database="bibliosesto"
    )

# Create SQLAlchemy engine
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, 
#     connect_args={"check_same_thread": False}
# )
# Per MySQL
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Per PostgreSQL
# engine = create_engine(PG_DATABASE_URL)
engine = create_engine("postgresql+psycopg2://innktnbgftlllfaggzow:urpxujxabqmbtmpkprbkvrtaqvkjss@9qasp5v56q8ckkf5dc.leapcellpool.com:6438/zekjptozpulnobhzqrlu?sslmode=require")

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for models
Base = declarative_base()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
