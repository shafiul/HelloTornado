from sqlalchemy import Column, Integer, String
import models.base

__author__ = 'shantanu'


class User(models.base.Base.instance().get_base()):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50))
    group = Column(Integer)
    password = Column(String(50))