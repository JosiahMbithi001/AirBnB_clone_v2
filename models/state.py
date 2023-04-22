#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, DateTime, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """ State Class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Return the list of City instances with
            state_id equals to the current State.id
            """
            city_values = models.storage.all(City).values()
            city_list = []
            for city in city_values:
                if city.state_id == self.id:
                    city_list.append(city)
                return city_list
