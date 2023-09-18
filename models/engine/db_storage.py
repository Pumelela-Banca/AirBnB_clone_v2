#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}', pool_pre_ping=True)

    def all(self, cls=None):
        dict1 = {}
        if cls is not None:
            for instance in session.query(cls.__name__):
                dict1[f'{instance.name}.{instance.id}'] = instance
            return dict1
        else:
            for instance in session.query(User, State, City, Amenity, Place, Review):
                dict1[f'{instance.name}.{instance.id}'] = instance
            return dict1
    
    def new(self, obj):
        self.__session.add(obj)
    
    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session(obj)

    def reload(self):
        Base.metadata.create_all(bind=self.__engine)
        SessionFactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        ScopedSessionFactory = scoped_session(SessionFactory)
        self.__session = ScopedSessionFactory()
