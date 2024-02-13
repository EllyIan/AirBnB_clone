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
    def _init_(User, name, email,password)
    super()._init_(name=name, email=email, password=password)

class(State) BaseModel:
    def _init_(user, name)
    super()._init_(name=name)

class(City) BaseModel:
    def _init_(user, name, state)
    super()._init_(name=name, state=state)
class(Place) BaseModel:
    def _init_(user, name, description, price, City)
    super()._init_(name=name, description=description, price=price, city=city)


