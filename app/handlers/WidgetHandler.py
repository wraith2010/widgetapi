import json
import tornado.web
from domain.Widget import Widget
from services.widgetService import WidgetService

class WidgetHandler(tornado.web.RequestHandler):

    def get(self):
        widget_list = []

        widget01 = Widget(1, 'large flange', 3)
        widget_list.append(widget01)

        widget02 = Widget(2, 'small flange', 5)
        widget_list.append(widget02)

        widget03 = Widget(3, 'funky flange', 20)
        widget_list.append(widget03)

        print(json.dumps([o.toJson() for o in widget_list]))

        return self.write(json.dumps([o.toJson() for o in widget_list]))

    def put(self):
        widget_list = []
        
        data_list = tornado.escape.json_decode(self.request.body)
 
        for data in data_list:
            WidgetService.save(Widget(data['name'],data['part_count']))
