import json
import pickle
from enum import Enum

class FileType(Enum):
    JSON = 1
    BYTE = 2

class SerializeManager:
    def __init__(self, filename, filetype):
        self.filename = filename
        self.filetype = filetype

    def __enter__(self):
        if self.filetype == FileType.JSON:
            self.file = open(self.filename, 'w')
        elif self.filetype == FileType.BYTE:
            self.file = open(self.filename, 'wb')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def serialize(self, obj):
        if self.filetype == FileType.JSON:
            with open(self.filename, 'w') as file:
                json.dump(obj, file)
        elif self.filetype == FileType.BYTE:
            with open(self.filename, 'wb') as file:
                file.write(pickle.dumps(obj))

def serialize(obj, filename, filetype):
    manager = SerializeManager(filename, filetype)
    manager.serialize(obj)


data = {"prop1": "value1", "prop2" : "value2"}
with SerializeManager("test_4.json", FileType.JSON) as user:
    user.serialize(data)
# print_file("test_4.json")


print(isinstance(serialize.__globals__['SerializeManager'], object))