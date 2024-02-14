#!/usr/bin/python3

'''This is the Module for BaseClass'''

import uuid
from datetime import  datetime


class BaseModel:

    """Abstract base class defining core functionality for the object hierarchy."""

    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        """
        Initializes a new BaseModel instance.
          
        Args:
            *args: Not used in this implementation.
            **kwargs: A dictionary containing attribute names and values.
        """

        if kwargs:
            # Exclude the '__class__' key from kwargs
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        # Convert string timestamps to datetime objects
                        try:
                            value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        except ValueError:
                            raise ValueError(f"Invalid datetime format for {key}: {value}")
                    setattr(self, key, value)
        else:
            self.id=str(uuid.uuid4())

        selfcreated_at_ = datetime.utcnow()
        selfupdated_at_ = datetime.utcnow()

        def save(self):

            """Records the current time as the last update."""

            self.updated_at = datetime.utcnow()

        def to_dict(self):

            """Implements the dict attribute to represent the instance as a dictionary."""

            inst_dict =self._dict_.copy()
            inst_dict["_class_"] = self._class_._name_
            inst_dict["created_at"] = self.created_at.isoformat()
            inst_dict["updated_at"] =self.updated_at.isoformat()

            return inst_dict

        def _str_(self):

            """Converts the object into a readable string."""

            class_name = self._class_._name_
            return"[{}] ({}) {}".format(class_name.self.id.self._dict_)

if __name__ == "_main_":
    my_model= BaseModel()
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

