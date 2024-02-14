#!/usr/bin/python3

'''This is the Module for BaseClass'''

import uuid
from datetime import  datetime
from models import storage

class BaseModel:
    """Abstract base class defining core functionality for the object hierarchy."""

    def _init_(self):
        self.id=(uuid.uuid4())

        selfcreated_at = datetime.utcnow()
        selfupdated_at = datetime.utcnow()

        def save(self):
            """Records the current time as the last update."""

            self.updated_at = datetime.utcnow()

        def to_dict(self):
        """Implements the __dict__ attribute to represent the instance as a dictionary."""

            inst_dict =self._dict_.copy()
            inst_dict["_class_"] = self._class_._name_
            inst_dict["created at"] = self.created_at.isoformat()
            inst_dict["updated_at"] =self.updated_at.isoformat()

            return inst_dict

        def _str_(self): 
            """Converts the object into a readable string."""

            class_name = self._class_._name_
            return"[{}] ({}) {}".format(class_name.self.id.self._dict_)

if _name_ =="_main_":
    my_model = BaseModel()
    my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

