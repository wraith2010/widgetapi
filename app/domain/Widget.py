import json

class Widget:

    def __init__(self, pid, name, part_count):
        self.pid = pid
        self.name = name
        self.part_count = part_count
        

    def toJson(self):    
        return json.dumps(self.__dict__)


# Name (utf8 string, limited to 64 chars)
# Number of parts (integer)
# Created date (date, automatically set)
# Updated date (date, automatically set)
