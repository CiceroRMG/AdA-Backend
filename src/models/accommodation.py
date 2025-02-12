from sqlalchemy import Column, Integer, String, Float, ARRAY
from src.db.database import Base

class AccommodationModel(Base):
    __tablename__ = "accommodation"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    image = Column(ARRAY(String), nullable=True)
    night_price = Column(Float, nullable=False)
    location = Column(String, index=True, nullable=False)
