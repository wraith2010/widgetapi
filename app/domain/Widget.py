import json


class Widget:

    def __init__(self, *args): 

        if len(args) > 1:
            self.name = args[0]
            self.part_count = args[1]

        elif len(args) == 1:
            row  = args[0]
            if 'pid' in row: 
                self.pid = row['pid']
            if 'name' in row: 
                self.name = row['name']
            if 'part_count' in row: 
                self.part_count = row['part_count']
            if 'Created' in row: 
                self.created = row['Created']
            if 'modified' in row: 
                self.modified = row['modified']

    def toJson(self):
        return json.dumps(self.__dict__)

# Name (utf8 string, limited to 64 chars)
# Number of parts (integer)
# Created date (date, automatically set)
# Updated date (date, automatically set)
