#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """tests for state class"""

    def __init__(self, *args, **kwargs):
        """initialise class"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """test name type"""
        new = self.value()
        self.assertEqual(type(new.name), str)
