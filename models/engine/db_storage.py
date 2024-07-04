#!/usr/bin/env python3
"""
Contains the class DBStorage
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

class DBStorage:
    __engine = None
    __session = None
    classes = [State, City, User, Amenity, Place, Review]  # List of all model classes

    def __init__(self):
        """Initializes the DBStorage instance."""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, password, host, database),
            pool_pre_ping=True)
        
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        # Initialize scoped_session
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        """Query on the current database session"""
        new_dict = {}
        try:
            if cls:
                if isinstance(cls, str):
                    cls = eval(cls)
                query = self.__session.query(cls).all()
                for obj in query:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    new_dict[key] = obj
            else:
                for clss in self.classes:
                    query = self.__session.query(clss).all()
                    for obj in query:
                        key = "{}.{}".format(obj.__class__.__name__, obj.id)
                        new_dict[key] = obj
        except Exception as e:
            print(e)
            self.__session.rollback()
        finally:
            return new_dict

    def new(self, obj):
        """Adds the object to the current database session."""
        try:
            self.__session.add(obj)
        except Exception as e:
            print(e)
            self.__session.rollback()

    def save(self):
        """Commits all changes of the current database session."""
        try:
            self.__session.commit()
        except Exception as e:
            print(e)
            self.__session.rollback()

    def delete(self, obj=None):
        """Deletes from the current database session obj if not None."""
        try:
            if obj:
                self.__session.delete(obj)
        except Exception as e:
            print(e)
            self.__session.rollback()

    def reload(self):
        """Reloads data from the database."""
        Base.metadata.create_all(self.__engine)


