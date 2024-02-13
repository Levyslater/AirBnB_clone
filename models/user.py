#!/usr/bin/python3
"""Handles User information"""

from models.base_model import BaseModel


class User(BaseModel):
    """class creates new user with below attributes
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
