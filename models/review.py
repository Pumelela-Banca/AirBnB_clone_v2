#!/usr/bin/python3

#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import os


env_val = os.environ.get('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base):
    """ reviews from users """
    if env_val == 'db':
        __tablename__ = "reviews"
        text = Column(
                String(1024),
                nullable=False)
        place_id = Column(
                String(60),
                ForeignKey("places.id"),
                nullable=False)
        user_id = Column(
            String(60),
            ForeignKey("users.id"),
            nullable=False)
        user = relationship("User")
        place = relationship("Place")
    else:
        text = ""
        user_id = ""
        place_id = ""
