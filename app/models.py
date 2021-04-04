from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Boolean, Date, ForeignKey
from sqlalchemy import func, join
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import numpy as np
import pandas as pd
import datetime

# setting up the database
engine = create_engine('sqlite:///data.db')
engine.connect()

Base = declarative_base()


class Agents(Base):
    # table for agents
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)

    def __repr__(self):
        return "<Agents(id={}, first_name={}, last_name={}, email={})".format(self.id, self.first_name, self.last_name, self.email)


class Offices(Base):
    # table for offices
    __tablename__ = 'offices'
    id = Column(Integer, primary_key=True)
    area = Column(String, index=True)

    def __repr__(self):
        return "<Offices(id={}, area={})".format(self.id, self.area)


class Sellers(Base):
    # table for sellers
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)

    def __repr__(self):
        return "<Sellers(id={}, first_name={}, last_name={}, email={})".format(self.id, self.first_name, self.last_name, self.email)


class Buyers(Base):
    # table for buyers
    __tablename__ = 'buyers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)

    def __repr__(self):
        return "<Buyers(id={}, first_name={}, last_name={}, email={})".format(self.id, self.first_name, self.last_name, self.email)


class Houses(Base):
    # table for houses
    __tablename__ = 'houses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    office_id = Column(Integer, ForeignKey('offices.id'))
    agent_id = Column(Integer, ForeignKey('agents.id'))
    seller_id = Column(Integer, ForeignKey('sellers.id'))
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    zipcode = Column(Integer)
    date = Column(Date)
    sold = Column(Boolean)

    def __repr__(self):
        return "<Houses(id={}, name={}, price={}, sold={})>".format(self.id, self.name, self.price, self.sold)


class Sales(Base):
    # table for sales
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    house_id = Column(Integer, ForeignKey('houses.id'))
    buyer_id = Column(Integer, ForeignKey('buyers.id'))
    sale_price = Column(Integer)
    sale_date = Column(Date)

    def __repr__(self):
        return "<Sales(id={}, house_id={}, buyer_id={})>".format(self.id, self.house_id, self.buyer_id)


class Commission(Base):
    # table for commissions for agents
    __tablename__ = 'commission'
    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('agents.id'))
    sale_id = Column(Integer, ForeignKey('sales.id'))
    commission = Column(Integer)

    def __repr__(self):
        return "<Commission(id={}, agent_id={}, commission={})>".format(self.id, self.agent_id, self.commission)
