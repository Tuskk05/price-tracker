from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config.settings import DATABASE_URL, SQLITE_CONNECT_ARGS

# Creation of the database engine
engine = create_engine(
    DATABASE_URL, 
    connect_args=SQLITE_CONNECT_ARGS if "sqlite" in DATABASE_URL else {}
)

# Creates sessions for using the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All tables will inherit from this class
Base = declarative_base()

# Generator function to get a database session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()