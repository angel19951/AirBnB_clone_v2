#!/usr/bin/python3
"""Module of storage (MySQL)
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import models


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ Contructor DB
        """
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        DB_URL = "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db)

        self.__engine = create_engine(DB_URL, pool_pre_ping=True)
        # Base.metadata.create_all(self.__engine)
        # Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # self.__session = Session()
        if getenv('HBNB_ENV') == 'test':
            Base.medata.drop_all(self.__engine)

    def all(self, cls=None):
        """all objects
        """
        classes = ['State', 'City', 'User', 'Place', 'Review', 'Amenity']
        objs = {}

        if cls is None:
            for class_nm in classes:
                query = self.__session.query(eval(class_nm)).all()
                for obj in query:
                    key = obj.__class__.__name__ + '.' + obj.id
                    objs[key] = obj
        else:
            query = self.__session.query(eval(cls)).all()
            for obj in query:
                key = obj.__class__.__name__ + '.' + obj.id
                objs[key] = obj
        return objs

    def new(self, obj):
        """New object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit in the DB
        """
        self.__session.commit()

    def delele(self, obj=None):
        """delete an object
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload  from DB
        """
        Base.metadata.create_all(self.__engine)
        r_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # self.__session = scoped_session(r_session)
        Session = scoped_session(r_session)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute
        """
        self.__session.close_all()
