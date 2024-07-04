from uuid import uuid4
from datetime import datetime, timezone
import sqlalchemy
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """Represents the BaseModel of the HBnB project."""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        timef = "%Y-%m-%dT%H:%M:%S.%f"  # Updated format to include microseconds
        if kwargs.get("id", None) is None:
            self.id = str(uuid4())
        else:
            self.id = kwargs["id"]

        if "created_at" in kwargs:
            self.created_at = datetime.strptime(kwargs["created_at"], timef)
        else:
            self.created_at = datetime.now()

        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(kwargs["updated_at"], timef)
        else:
            self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                self.__dict__[k] = v

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        rdict = self.__dict__.copy()
        if "_sa_instance_state" in rdict:
            del rdict["_sa_instance_state"]
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, rdict)

    
    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance."""
        rdict = {k: v for k, v in self.__dict__.items() if k != '_sa_instance_state'}
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)