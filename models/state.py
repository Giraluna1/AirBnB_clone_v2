#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref="states", cascade="delete")
    else:
        name = ''

        @property
        def cities(self):
            """method definition for cities"""
            from models import storage
            city_list = []
            for key, value in storage.all('City').items():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
