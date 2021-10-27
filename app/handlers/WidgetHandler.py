import json
import tornado.web
from domain.Widget import Widget


class WidgetHandler(tornado.web.RequestHandler):
    def get(self):
        widget_list = []

        widget01 = Widget(1, 'large flange', 3)
        widget_list.append(widget01)

        widget02 = Widget(2, 'small flange', 5)
        widget_list.append(widget02)

        widget03 = Widget(3, 'funky flange', 20)
        widget_list.append(widget03)

        return self.write(json.dumps([o.toJson() for o in widget_list]))
