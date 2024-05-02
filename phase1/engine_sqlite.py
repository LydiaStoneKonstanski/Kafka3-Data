from kafka import KafkaConsumer, TopicPartition
from sqlalchemy import Column, Integer, String, DECIMAL, create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from json import loads


Base = declarative_base()
class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    custid = Column(Integer)
    type = Column(String(250), nullable=False)
    date = Column(Integer)
    amt = Column(DECIMAL)

    def __init__(self, custid, type, date, amt):
        self.custid = custid
        self.type = type
        self.date = date
        self.amt = amt

engine = create_engine(f'sqlite:///zipbank.sqlite')
Base.metadata.create_all(engine)

# metadata = MetaData(bind=engine)
session = Session(bind=engine)

