#!/usr/bin/python3
"""Class BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __ini__(self, *args, **kwargs):
        """"""
        super().__ini__(*args, **kwargs)
    