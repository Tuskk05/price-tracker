from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

# Represents the products that we track
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False)
    target_price = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # A product can have many PriceHistory entries
    prices = relationship("PriceHistory", back_populates="product", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Product(name={self.name}, url={self.url})>"

#Stores all the data from different products
class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    price = Column(Float, nullable=False)
    currency = Column(String, default="EUR")
    scraped_at = Column(DateTime, default=datetime.utcnow)

    # It can only belong to one product
    product = relationship("Product", back_populates="prices")

    def __repr__(self):
        return f"<PriceHistory(price={self.price}, date={self.scraped_at})>"