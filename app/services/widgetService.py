import sqlite3
from domain.Widget import Widget


class WidgetService:

    def getConnection():
        connection = sqlite3.connect('database/widget.db')
        connection.row_factory = sqlite3.Row
        return connection

    def update(widget):
        connection = WidgetService.getConnection()
        connection.execute("UPDATE widgets SET name = ?, partCount = ? WHERE pid = ?;",
                           (widget.name, widget.partCount, widget.pid))
        connection.commit()

    def save(widget):
        connection = WidgetService.getConnection()
        connection.execute(
            "INSERT INTO widgets (name, partCount) VALUES (?, ?);", (widget.name, widget.partCount))
        connection.commit()

    def list():
        widget_List = []
        connection = WidgetService.getConnection()
        cursor = connection.execute("SELECT * FROM widgets;")
        for row in cursor:
            widget_List.append(Widget(row))

        return widget_List

    def retrieve(pid):
        widget_List = []
        connection = WidgetService.getConnection()
        cursor = connection.execute(
            "SELECT * FROM widgets WHERE pid = ?;", pid)
        for row in cursor:
            widget_List.append(Widget(row))

        return widget_List

    def delete(pid):
        connection = WidgetService.getConnection()
        connection.execute("DELETE FROM widgets WHERE pid = ?;", pid)
        connection.commit()
