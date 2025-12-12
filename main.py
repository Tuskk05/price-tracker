from src.database import engine, Base
from src.models import Product, PriceHistory

def init_db():
    """Create database tables based on models"""
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")

if __name__ == "__main__":
    init_db()