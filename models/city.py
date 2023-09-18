#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
import os


env_value = os.environ.get('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if env_value == 'db':
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
    else:
        name = ""
        state_id = ""
