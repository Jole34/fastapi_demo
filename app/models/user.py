from db.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime, func, Boolean

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    created_om = Column(DateTime, server_default=func.now())
    hashed_password = Column(String, nullable=False)
    active = Column(Boolean, nullable=True, default=False)
    name = Column(String, nullable=False)
