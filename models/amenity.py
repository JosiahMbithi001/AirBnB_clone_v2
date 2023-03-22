#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
<<<<<<< HEAD
=======
from sqlalchemy.orm import relationship
>>>>>>> 7c4eaa4e39985e3f8cbcda7a503732c96d3f30f9


class Amenity(BaseModel, Base):
    """A class that creates different amenities"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
