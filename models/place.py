#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models import storage
from models.amenity import Amenity
from models import HBNB_TYPE_STORAGE

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    reviews = relationship(
        "Review", cascade="all, delete", backref="place")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False, overlaps='place_amenities')

    amenity_ids = []

    if HBNB_TYPE_STORAGE != 'db':
        @property
        def amenities(self):
            '''returns the list of Amenity instances based on
            the attribute amenity_ids
            contains all Amenity.id linked to the Place'''
            amenity_list = []
            for amenity in list(storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            '''handles append method for adding an Amenity.id
            to the attribute amenity_ids'''
            '''set am'''
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)

        @property
        def reviews(self, place_id):
            """"returns the list of Review instances with
            place_id equals to the current Place.id"""
            from models.review import Review
            all_reviews = self.all(Review)
            reviews_list = []
            for review in all_reviews.values():
                if review.place_id == place_id:
                    reviews_list.append(review)
            return reviews_list
