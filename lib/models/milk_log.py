from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class MilkLog(Base):
    __tablename__ = 'milk_logs'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    quantity = Column(Float, nullable=False)
    farmer_id = Column(Integer, ForeignKey('farmers.id'))

    farmer = relationship("Farmer", back_populates="milk_logs")
