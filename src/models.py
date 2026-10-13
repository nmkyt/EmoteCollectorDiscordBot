import os
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


# Настройка подключения к базе данных PostgreSQL
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = sqlalchemy.orm.declarative_base()


class Message(Base):
    __tablename__ = 'messages'
    message_id = Column(BigInteger, primary_key=True)
    correct_reaction = Column(String)
    end_time = Column(DateTime)


class Reaction(Base):
    __tablename__ = 'reactions'
    message_id = Column(BigInteger, ForeignKey('messages.message_id'), primary_key=True)
    user_id = Column(BigInteger, primary_key=True)
    reaction = Column(String)


class Score(Base):
    __tablename__ = 'scores'
    user_id = Column(BigInteger, primary_key=True)
    score = Column(Integer, default=0)


Base.metadata.create_all(engine)

