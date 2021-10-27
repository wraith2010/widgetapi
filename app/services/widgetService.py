import sqlite3
from domain.Widget import Widget

class WidgetService:

    def getConnection():
        return sqlite3.connect('D:\\databases\\widget.db')

    def save(widget):
        
        connection = WidgetService.getConnection()
        connection.execute("INSERT INTO widgets (name, partCount) VALUES (?, ?);",(widget.name,widget.part_count))
        connection.commit()

        print("saving %s", widget.toJson)


