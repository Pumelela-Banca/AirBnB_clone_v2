#!/usr/bin/python3
""" Module for testing file storage"""
import os
import unittest
import MySQLdb
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User


env_val = os.environ.get('HBNB_TYPE_STORAGE')


@unittest.skipIf(env_val != 'db', 'Not a DB run')
class TestDB(unittest.TestCase):
    """ Class to test the file storage method """
    def test_save(self):
        """
        test if objects are added to db
        """
        one = User(first_name="Sbu", last_name="Ndebele",
                   password="123", email="viet@zoom.com")
        # save to db
        one.save()
        # look for one in saved values
        self.assertTrue(one in storage.all().values())
        # find one in DB
        enginDB = MySQLdb.connect(host=os.environ.get('HBNB_MYSQL_HOST'),
                                  user=os.environ.get("HBNB_MYSQL_USER"),
                                  passwd=os.environ.get("HBNB_MYSQL_PWD"),
                                  port=3306,
                                  db=os.environ.get("HBNB_MYSQL_DB"))
        cursor = enginDB.cursor()
        cursor.execute("SELECT * FROM users WHERE id='{}'".format(one.id))
        info = cursor.fetchone()
        self.assertTrue(info is not None)
        self.assertIn("Sbu", info)
        self.assertIn("Ndebele", info)
        self.assertIn("123", info)
        self.assertIn("viet@zoom.com", info)
        self.assertIn(f"User.{one.id}", storage.all(User).keys())
        cursor.close()
        enginDB.close()

    def test_delete(self):
        """
        Tests to see if files are deleted
        """
        two = User(first_name="Sbu", last_name="Ndebele",
                   password="123", email="viet@zoom.com")
        enginDB = MySQLdb.connect(host=os.environ.get('HBNB_MYSQL_HOST'),
                                  user=os.environ.get("HBNB_MYSQL_USER"),
                                  passwd=os.environ.get("HBNB_MYSQL_PWD"),
                                  port=3306,
                                  db=os.environ.get("HBNB_MYSQL_DB"))
        two.save()
        # find two in engine
        self.assertTrue(two in storage.all().values())
        cursor = enginDB.cursor()
        cursor.execute("SELECT * FROM users WHERE id='{}'".format(two.id))
        info = cursor.fetchone()
        self.assertTrue(info is not None)
        self.assertIn("Sbu", info)
        self.assertIn("Ndebele", info)
        self.assertIn("123", info)
        self.assertIn("viet@zoom.com", info)
        self.assertIn(f"User.{two.id}", storage.all(User).keys())
        two.delete()
        self.assertNotIn(f"User.{two.id}", storage.all(User).keys())
        cursor.close()
        enginDB.close()

    def test_reload(self):
        """
        test if instance can be reloaded
        """
        engineDB = MySQLdb.connect(host=os.environ.get('HBNB_MYSQL_HOST'),
                                  user=os.environ.get("HBNB_MYSQL_USER"),
                                  passwd=os.environ.get("HBNB_MYSQL_PWD"),
                                  port=3306,
                                  db=os.environ.get("HBNB_MYSQL_DB"))
        cursor = engineDB.cursor()
        cursor.execute(
            """INSERT INTO users(id, created_at, updated_at, email, password
            first_name, last_name) VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            ("holder",
             str(datetime.now()),
             str(datetime.now()),
             "alex@moo",
             "password",
             "Alex",
             "Brown"))
        self.assertNotIn("User.holder", storage.all())
        self.assertNotIn("alex@moo", storage.all())
        engineDB.commit()
        storage.reload()
        self.assertIn("User.holder", storage.all())
        self.assertIn("alex@moo", storage.all())
        self.assertIn("password", storage.all())
        cursor.close()
        engineDB.close()

    def test_save(self):
        """
        Tests if instance is saved in DB
        """
        three = User(
            first_name="Naru", last_name="Uzu",
            password="rasen", email="NA@HL.com"
        )
        engineDB = MySQLdb.connect(host=os.environ.get('HBNB_MYSQL_HOST'),
                                  user=os.environ.get("HBNB_MYSQL_USER"),
                                  passwd=os.environ.get("HBNB_MYSQL_PWD"),
                                  port=3306,
                                  db=os.environ.get("HBNB_MYSQL_DB"))
        cursor = engineDB.cursor()
        pass

    def test_new(self):
        """test if new can be used to add
        new item to DB"""
        pass

    def test_all(self):
        """
        test if all works
        """
        pass
