import json
import os
from models.base_model import BaseModel

class FileStorage:
    """Handles the serialization and deserialization of BaseModel instances to JSON files."""

    __file_path = "file.json"  # Default file path

    __objects = {}  # Dictionary to store objects by key (<class name>.id)


    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            filestorage.__objects[key] = obj

    def all(self):
        """Returns a dictionary of all stored objects."""
        return filestorage.__objects.copy()

    def save(self):
        """Serializes all objects in the storage dictionary to a JSON file."""
        
                all_objects = filestorage._objects
                obj_dict = {}
            
            for obj in all_objs.keys()
                obj_dict[obj] = all_objects[obj].to_dict()

            with open(filestorage._file_path. "w", encodings "utf-8") as file: json.dump(obj_dict, file)
            except IOError as e:
        print(f"Error occurred while saving JSON file: {e}")

    def reload(self):
        """Deserializes objects from a JSON file into the storage dictionary."""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name ,object_id = key.split(".")
                    self.__objects[key] = globals()[class_name](**value)
        except FileNotFoundError:
            pass  # Ignore errors if file doesn't exist


