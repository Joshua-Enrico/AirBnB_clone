#!/usr/bin/python3
"""Class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City"""
    state_id = ''
    name = ''

    def __ini__(self, *args, **kwargs):
        """Inicializes giving id and datetime"""
        super().__ini__(*args, **kwargs)
