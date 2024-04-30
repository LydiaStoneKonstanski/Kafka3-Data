from kafka import KafkaConsumer, TopicPartition
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Metadata
from json import loads
import name_password

host ='localhost',
user = name_password.username,
passwd = name_password.password
Base = declarative_base()
class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    custid = Column(Integer)
    type = Column(String(250), nullable=False)
    date = Column(Integer)
    amt = Column(Integer)

    def __init__(self, custid, type, date, amt):
        self.custid = custid
        self.type = type
        self.date = date
        self.amt = amt

engine = create_engine(f'mysql://{user}:{passwd}@{host}/kafka_example')
Base.metadata.create_all(engine)
metadata = MetaData(bind=engine)
session = Session()