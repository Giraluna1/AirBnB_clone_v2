#!/usr/bin/python3
""" This module define the Class Data Base for hbnb clone """

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ class DBStorage mange the querys for the user"""
    __engine = None
    __session = None

    def __init__(self):
        """
        instance method engine that liked to the MySQL DB
        and user created
        """
        credentials = (
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB'))

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(*credentials), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            # drop all tables
            pass

    def all(self, cls=None):
        """
        This method query on the current database session
        all objects depending of the class name
        """
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

        result = {}
        if cls:
            if type(cls) is not str:
                cls = cls.__name__
            query = self.__session.query(classes[cls]).all()
            for obj in query:
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                result[key] = obj

        else:
            for clas in classes:
                query = self.__session.query(classes[clas]).all()
                for obj in query:
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    result[key] = obj
        return result

    def new(self, obj):
        """ add the object of the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current DB session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current DB session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the DB """
        # generate database schema
        Base.metadata.create_all(self.__engine)

        # create a new session
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        #Session = scoped_session(session_factory)
        self.__session = scoped_session(session_factory)

    def close(self):
        """ Close session """
        self.__session.remove()
