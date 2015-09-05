
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, Float, String, \
	DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSON, ARRAY

Base = declarative_base()

class Fact(Base):
	__tablename__ = 'facts'
	id = Column(Integer, primary_key=True)
	datetime = Column(DateTime, index=True)
	snow = Column(Boolean)
	humidity = Column(Integer)  # percentage
	temperature = Column(Float)  # degrees c
	precipitation = Column(Float)  # mm