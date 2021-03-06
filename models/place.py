#!/usr/bin/python3
"""This is the place class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import MetaData, Float, Table
from sqlalchemy.orm import relationship, backref
from os import environ


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id",
                             String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id",
                             String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", cascade="all, delete", backref="place")


    @property
    def reviews(self):
        """ Return the list of the review
        """
        reviews = []
        reviews_list = models.storage.all(Review)
        for review in reviews_list.values():
            if review.place_id == self.id:
                reviews.append(review)
        return reviews

    if environ.get('HBNB_TYPE_STORAGE') == "db":
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False)

    else:
        @property
        def amenities(self):
            """amenities getter property for FileStorage
            """
            amenities = models.storage.all(models.Amenity)
            place_amenities = []
            for obj_amenities in amenities.values():
                for a_id in amenity_ids:
                    if a_id == obj_amenities.id:
                        place_amenities.append(obj_amenities)
            return place_amenities

        @amenities.setter
        def amenities(self, obj):
            """amenities setter property for FileStorage
            """
            if isinstance(obj, models.Amenity):
                self.amenity_ids.append(obj.id)
