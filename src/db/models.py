from sqlalchemy import Column, String, Integer, Boolean, Float, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base


async def wrapped_models(Base: declarative_base):
    class Swaps(Base):
        __tablename__ = 'swaps'

        id = Column(Integer, primary_key=True, autoincrement=True)
        timestamp = Column(Integer)
        block = Column(Integer)
        pool_contract = Column(String)
        amount0 = Column(String)
        amount1 = Column(String)
        price = Column(Float)

    class Pools(Base):
        __tablename__ = 'pools'

        id = Column(Integer, primary_key=True, autoincrement=True)
        pool_contract = Column(Integer)
        token0 = Column(String)
        token1 = Column(String)

    class Future(Base):
        __tablename__ = 'future'
        id = Column(Integer, primary_key=True, autoincrement=True)
        pool_contract = Column(String)
        timestamp = Column(Integer)
        price = Column(Float)
        price_upper = Column(Float)
        price_lower = Column(Float)

    return Swaps, Pools, Future
