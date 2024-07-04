"""
FileStorage class model
"""
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

class FileStorage:
    """
    serializes instances to JSON file
    also
    deserializes JSON file to an instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
    Returns a dictionary of models currently in storage.

    Args:
        cls (class, optional): If specified, filters the result to include
            only objects of the specified class.

    Returns:
        dict: A dictionary containing objects in storage.
    """
        cls_dict = {}
        if cls:
            if isinstance(cls, str):
                cls = globals().get(cls)

            if cls and issubclass(cls, BaseModel):
                for k, v in self.__objects.items():
                    if isinstance(v, cls):
                        cls_dict[k] = v
        else:
            cls_dict = self.__objects
        
        return cls_dict

    
    def new(self, obj):
        """
        Setting in __objects
        the `obj` with key <obj class name>.id method
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes a set of
        __objects to JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for x, y in self.__objects.items():
                dict_storage[x] = y.to_dict()
            json.dump(dict_storage, f)


    def reload(self):
        """
        Deserializes the JSON
        file to __objects
        nb: Only if it exists!
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
        
    def delete(self, obj=None):
        """
        Delete obj from __objects if it’s inside - if obj is equal to None,
        the method should not do anything
        """
        if obj == None:
            return
        del_obj = "{}.{}".format(obj.__class__.__name__, obj.id)

        try:
            del FileStorage.__objects[del_obj]
        except AttributeError:
            pass
        except KeyboardInterrupt:
            pass