from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..database import MyBase


class User(MyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    