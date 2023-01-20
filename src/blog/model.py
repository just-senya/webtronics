from sqlalchemy import Column, String, Text, Integer
from sqlalchemy.orm import relationship

from ..database import MyBase


class Blog(MyBase):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)