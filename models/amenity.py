#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """A class that creates different amenities"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
