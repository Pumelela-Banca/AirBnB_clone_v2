#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Test class for reviews"""

    def __init__(self, *args, **kwargs):
        """review initialisation"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test if id is string"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """test if id is string """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """test if text is string """
        new = self.value()
        self.assertEqual(type(new.text), str)
