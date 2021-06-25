#!/usr/bin/python3
"""Class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents a City"""
    name = ''

    def __ini__(self, *args, **kwargs):
        """"""
        super().__ini__(*args, **kwargs)
