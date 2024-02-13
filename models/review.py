#!/usr/bin/python3
"""Client Reviews about a place"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    class that contains the Review
    """
    user_id = ""
    place_id = ""
    text = ""
