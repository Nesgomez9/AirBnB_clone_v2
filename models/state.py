#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, backref
import models
from os import environ


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if environ.get('HBNB_TYPE_STORAGE') == "db":
        cities = relationship('City', backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """ Return the list of the city with the same if os self.id"""
            cities = models.storage.all(City)
            states = []
            for city in cities.values():
                if city.state_id == self.id:
                    states.append(city)
            return states
