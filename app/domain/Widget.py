import json


class Widget:

    def __init__(self, *args):

        if len(args) > 1:
            self.name = args[0]
            self.partCount = args[1]

        elif len(args) == 1:
            row = args[0]
            self.pid = row['pid']
            self.name = row['name']
            self.partCount = row['partCount']
            self.created = row['created']
            self.modified = row['modified']

    def toJson(self):
        return json.dumps(self.__dict__)

# Name (utf8 string, limited to 64 chars)
# Number of parts (integer)
# Created date (date, automatically set)
# Updated date (date, automatically set)
