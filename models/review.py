#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ reviews from users """
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
