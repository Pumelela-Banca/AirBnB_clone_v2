#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy import Float
from sqlalchemy.orm import relationship
import os


env_val = os.environ.get('HBNB_TYPE_STORAGE')


place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id"),
            primary_key=True,
            nullable=False),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id"),
            primary_key=True,
            nullable=False)
        )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    if env_val == 'db':
        reviews = relationship("Review", backref="place", cascade='delete')
        amenities = relationship(
                "Amenity",
                secondary=place_amenity,
                back_populates="place_amenities",
                viewonly=False)
    else:
        @property
        def reviews(self):
            """Returns the list of Review instances with
               place_id equals to the current Place.id
            """
            from models.__init__ import storage
            dict_reviews = storage.all(Review)
            reviews_list = []
            for rev in dict_reviews.values():
                if rev.place_id == self.id:
                    reviews_list.append(rev)
            return reviews_list

        @property
        def amenities(self):
            """returns the list of Amenity instances
               based on the attribute amenity_ids
               that contains all Amenity.id linked to the Place
            """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, amenity_obj):
            if isinstance(amenity_obj, Amenity):
                if amenity_obj.id not in self.amenity_ids:
                    self.amenity_ids.append(amenity_obj.id)
