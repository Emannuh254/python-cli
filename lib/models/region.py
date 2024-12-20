from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Region(Base):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    director_id = Column(Integer, ForeignKey('directors.id'))

    director = relationship("Director", back_populates="region")
    farmers = relationship("Farmer", back_populates="region")
    collectors = relationship("Collector", back_populates="region")
