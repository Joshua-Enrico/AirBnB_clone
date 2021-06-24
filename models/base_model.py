#!/usr/bin/python3
"""Class BaseModel"""

import uuid
from datetime import datetime

"""Date format we must use"""
Dtime = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """"""

    def __ini__(self, *args, **kwargs):
        """Initialize a BaseModel"""
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)
            if hasattr(self, 'created_at') and type(self.create_at) is str:
                self.create_at = datetime.strptime(kwargs["create_at"], Dtime)
            if hasattr(self, 'updated_at') and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], Dtime)

        else:
            self.id = str(uuid.uud4)
            self.create_at = datetime.now()
            self.update_at = self.create_at

    def __str__(self):
        """str representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates the public ins attr upd_at with the curren one"""
        self.update_at = datetime.now()

    def to_dict(self):
        """ returns a dic containing keys and values of the instance"""
        