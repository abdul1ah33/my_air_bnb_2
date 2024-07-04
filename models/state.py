"""Defines the State class."""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_t


class State(BaseModel, Base):
    """Represent a state."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)


    if models.storage_t == 'db':
        cities = relationship("City", cascade="all, delete-orphan", backref="state")
    else:
        @property
        def cities(self):
            from models import storage
            cities_list = []
            for city in storage.all(City):
                if City.state_id == self.id:
                    cities_list.append(city)
            return cities_list