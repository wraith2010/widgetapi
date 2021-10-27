import json
import tornado.web
from domain.Widget import Widget
from services.widgetService import WidgetService


class WidgetHandler(tornado.web.RequestHandler):

    def get(self):
        return self.write(json.dumps([o.toJson() for o in WidgetService.list()]))

    def get(self, **kwargs):

        if len(kwargs.keys()) == 0:
            return self.write(json.dumps([o.toJson() for o in WidgetService.list()]))

        return self.write(json.dumps([o.toJson() for o in WidgetService.retrieve(kwargs['pid'])]))

    def put(self, **kwargs):

        data_list = tornado.escape.json_decode(self.request.body)

        for data in data_list:
            WidgetService.save(Widget(data['name'], data['part_count']))

    def post(self, **kwargs):
        data_list = tornado.escape.json_decode(self.request.body)

        for data in data_list:
            print(data)
            WidgetService.update(Widget(data))

    def delete(self, **kwargs):
        if len(kwargs.keys()) == 1:
            WidgetService.delete(kwargs['pid'])
        
