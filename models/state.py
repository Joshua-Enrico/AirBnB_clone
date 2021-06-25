#!/usr/bin/python3
"""Class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state"""
    name = ''

    def __ini__(self, *args, **kwargs):
        """Inicializes giving id and datetime"""
        super().__ini__(*args, **kwargs)
