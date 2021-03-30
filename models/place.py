#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import getenv
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), nullable=False, primary_key=True),
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), nullable=False, primary_key=True)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', cascade='delete')
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            back_populates='place_amenities',
            viewonly=False
        )

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """return the list of reviews"""
            from models import storage
            review_list = []
            for key, value in storage.all('Review').items():
                if value.place_id == self.id:
                    review_list.append(value)
            return review_list

        @property
        def amenities(self):
            """returns a list of amenities"""
            obj = []
            from models import storage
            for key, value in storage.all('Amenity').items():
                if self.amenity_ids in value.id:
                    obj.append(value)
            return obj

        @amenities.setter
        def amenities(self, amenities):
            """return"""
            if amenities.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(amenities)
