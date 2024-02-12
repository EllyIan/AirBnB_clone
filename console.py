#!/usr/bin/python3

"""Airbnb command interpreter to manage my objects"""

import click
import cmd
import json
import re
from .basemodel import BaseModel
from .models import User, State, City, Place
from .storage import save_object, load_object

class(user) BaseModel:
    def _init_(User, Name, Email, Password)
    super()._init_(Name=Name, Email=Email, Password=Password)

class(State) BaseModel:
    def _init_(User, Name)
    super()._init_(Name=Name)

class(City) BaseModel:
    def _init_(User, Name, State)
    super()._init_(Name=Name, State=State)


