#!/usr/bin/python3
"""Physical address and other other attributes"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    class that contains the Place name
    """
    city_id = ""
    name = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
