class NestedDict:
    def __init__(self, data):
        self._data = data  # Initialize with the provided nested dictionary

    def __getattr__(self, attr):
        if attr in self._data:  # Check if the attribute exists in the dictionary
            if isinstance(self._data[attr], dict):
                return NestedDict(self._data[attr])  # Create a new NestedDict if the attribute is a dictionary
            else:
                return self._data[attr]  # Return the attribute value
        else:
            raise AttributeError(f"'NestedDict' object has no attribute '{attr}'")

    def __setattr__(self, attr, value):
        if attr == "_data":
            super().__setattr__(attr, value)
        else:
            self._data[attr] = value  # Set the attribute value in the dictionary

    def get(self, key, default=None):
        return self._data.get(key, default)  # Get the value for the given key with an optional default

    def to_dict(self):
        return self._data  # Return the underlying dictionary


class Data:
    def __init__(self, **kwargs):
        self._data = kwargs  # Initialize with the provided keyword arguments

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)  # Instantiate the class using the provided dictionary as keyword arguments

    def to_dict(self):
        return self._data  # Return the underlying dictionary

    def __getattr__(self, attr):
        if attr in self._data:  # Check if the attribute exists in the dictionary
            if isinstance(self._data[attr], dict):
                return NestedDict(self._data[attr])  # Create a new NestedDict if the attribute is a dictionary
            else:
                return self._data[attr]  # Return the attribute value
        else:
            raise AttributeError(f"'Data' object has no attribute '{attr}'")

    def __setattr__(self, attr, value):
        if attr == "_data":
            super().__setattr__(attr, value)
        else:
            self._data[attr] = value  # Set the attribute value in the dictionary

    def __dir__(self):
        return list(self._data.keys())  # Return a list of keys as available attributes

    def __getitem__(self, key):
        return self._data[key]  # Get the value associated with the given key

    def __setitem__(self, key, value):
        self._data[key] = value  # Set the value for the given key


data = {
    "id": "1",
    "name": "first",
    "metadata": {
        "system": {
            "size": 10.7
        },
        "user": {
            "batch": 10
        }
    }
}

# load from dict
my_inst_1 = Data.from_dict(data)

# load from inputs
my_inst_2 = Data(name="my")

# reflect inner value
print(my_inst_1.metadata.system.size)  # should print 10.7

# default values
print(my_inst_1.metadata.system.get("height", 100))  # should print 100
print(my_inst_1.to_dict()['metadata']['system'].get('height', 100))  # should print 100

# autocomplete
print(my_inst_1.metadata)  # should print the metadata NestedDict object
