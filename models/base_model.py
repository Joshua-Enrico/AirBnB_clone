#!/usr/bin/env python3
"""Module of Base Model"""
from uuid import uuid4


class BaseModel:
    """BaseModel class definition"""

    def __init__(self, *args, **kwargs):
        """Constructor of the class"""
        
        for key, value in kwargs.items():
            setattr(self, key, value)

        if "id" not in kwargs.keys():
            self.id = str(uuid4())

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model.name)
print(my_model.my_number)
print(my_model.id)
