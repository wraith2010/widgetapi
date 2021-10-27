import tornado.web
from domain.Widget import Widget

class WidgetHandler(tornado.web.RequestHandler):
    def get(self):
        widget01 = Widget(1, 'large flange', 3)
        return self.write(widget01.toJson())
