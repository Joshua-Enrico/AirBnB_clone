#!/usr/bin/python3
"""Class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __ini__(self, *args, **kwargs):
        """Inicializes giving id and datetime"""
        super().__ini__(*args, **kwargs)
