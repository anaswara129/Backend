from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://postgres:Anaswara%40129@localhost/studentdb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocomit=False,
    autoflush=False,
    bind=engine 
)

Base = declarative_base()