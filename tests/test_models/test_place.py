#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Place tests"""

    def __init__(self, *args, **kwargs):
        """Place"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """test if id is string"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Test id type"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ test description type"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """test  type for number of rooms """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test  type for number of bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test  type for number of guests"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test type for night stays"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ test  type for location  lat"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """test  type for location long """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """test type for amenity"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
