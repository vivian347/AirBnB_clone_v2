#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
import models
from models.city import City


class State(BaseModel):
    """ State class """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tabename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                                cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            city_dict = model.storage.all(City)
            state_query = self.id
            city_list = []
            for k, v in city_dict.items():
                if v.state_id == self.id:
                    city_list.apend(v)
            return city_list
