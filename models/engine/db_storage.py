#!/usr/bin/python3
"""This is the class for DataBasetorage of the project AirBnB"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
from models.base_model import Base
from models.state import State

class DBStorage:
    """DBStorage class
    Attributes:
    __engine:
    _session:
    """

    __engine = None
    __session = None

    def __init__(self):
        """Declaration of the DBSstorage class
        """
        User = environ.get('HBNB_MYSQL_USER')
        Psswd = environ.get('HBNB_MYSQL_PWD')
        Host = environ.get('HBNB_MYSQL_HOST')
        Db = environ.get('HBNB_MYSQL_DB')
        Env = environ.get('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(User, Psswd, Host, Db),
                                      pool_pre_ping=True)
        if Env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Show all objects of a class
        """
        session = self.__session
        objects_dict = {}
        if cls:
            objects = session.query(cls).all()
            for obj in objects:
                key ="{}.{}".format(type(obj).__name, on.__id)
                objects_dict[key] = obj
        else:
            clases =[User, State, City, Amenity, Place, Review]
            for clas in clases:
                objects = session.query(cls).all()
            for obj in objects:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects_dict[key] = obj
        return ob_dict


    def new(self, obj):
        """new method
        """
        self.__session.add(obj)

    def save(self):
        """save method
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete method
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload method
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
