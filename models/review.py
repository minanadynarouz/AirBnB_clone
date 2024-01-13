#!/usr/bin/python3
"""Review inherits from the BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class"""
    place_id = ""
    user_id = ""
    text = ""
