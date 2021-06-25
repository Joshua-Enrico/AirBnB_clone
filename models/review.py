#!/usr/bin/python3
"""Class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review"""
    place_id = ''
    user_id = ''
    text = ''

    def __ini__(self, *args, **kwargs):
        """Inicializes giving id and datetime"""
        super().__ini__(*args, **kwargs)
