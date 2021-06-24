#!/usr/bin/python3
"""
Class BaseModel
"""

from datetime import datetime
import uuid
Dtime = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Base Model"""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel"""
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)
            if hasattr(self, 'created_at') and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], Dtime)
            if hasattr(self, 'updated_at') and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], Dtime)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """str representation"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the public ins attr upd_at with the curren one"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dic containing keys and values of the instance"""
        n_dict = self.__dict__.copy()
        if "created_at" in n_dict:
            n_dict["created_at"] = n_dict["created_at"].strftime(Dtime)
        if "updated_at" in n_dict:
            n_dict["updated_at"] = n_dict["updated_at"].strftime(Dtime)
        n_dict["__class__"] = self.__class__.__name__
        return n_dict

"""no puedo correr el test del archivo test"""
"""por eso pongo el test aqui"""
my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

"""aqui se testea kwargs"""
print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)