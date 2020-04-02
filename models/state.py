#!/usr/bin/python3
"""This is the state class"""

import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """ Return the list of the city with the same if os self.id"""
        cities = models.storage.all(City)
        states = []
        for city in cities.values():
            if city.state_id == self.id:
                states.append(city)
        return states
