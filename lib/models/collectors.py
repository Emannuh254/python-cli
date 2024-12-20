from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Collector(Base):
    __tablename__ = 'collectors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    contact_number = Column(String(15), nullable=True)
    region = Column(String(50), nullable=True)
    total_collected = Column(Float, nullable=False)

    def __init__(self, name, contact_number, region, total_collected):
        self.name = name
        self.contact_number = contact_number
        self.region = region
        self.total_collected = total_collected

    def __repr__(self):
        return f"<Collector(name={self.name}, region={self.region}, total_collected={self.total_collected})>"

engine = create_engine('sqlite:///milk_collector.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_collector(name, contact_number, region, total_collected):
    new_collector = Collector(name=name, contact_number=contact_number, region=region, total_collected=total_collected)
    session.add(new_collector)
    session.commit()

def view_collectors():
    collectors = session.query(Collector).all()
    for collector in collectors:
        print(f"ID: {collector.id} | Name: {collector.name} | Region: {collector.region} | Total Collected: {collector.total_collected}L")

def find_collector(name):
    collector = session.query(Collector).filter(Collector.name.ilike(f'%{name}%')).all()
    if collector:
        for c in collector:
            print(f"ID: {c.id} | Name: {c.name} | Region: {c.region} | Total Collected: {c.total_collected}L")
    else:
        print("Collector not found.")

def delete_collector(id):
    collector_to_delete = session.query(Collector).filter(Collector.id == id).first()
    if collector_to_delete:
        session.delete(collector_to_delete)
        session.commit()
        print(f"Collector with ID {id} deleted successfully.")
    else:
        print(f"Collector with ID {id} not found.")
