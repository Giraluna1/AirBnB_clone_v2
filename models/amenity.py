#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            'Place',
            secondary='place_amenity',
            back_populates='places',
            cascade='delete'
        )
    else:
        name = ""
