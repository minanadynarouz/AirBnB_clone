#!/usr/bin/python3
"""City inheriting from the BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Class"""
    name = ""
    state_id = ""
