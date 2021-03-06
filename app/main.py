import tornado.ioloop
import tornado.web

from handlers.WidgetHandler import WidgetHandler


class MainHandler(tornado.web.RequestHandler):
    html = '<html><head><title>widget api</title></head><body style="text-align:center;"><h1>Widget API Server is Live</h1></body></html>'

    def get(self):
        self.write(MainHandler.html)

    def make_app():
        # URL Mapping
        return tornado.web.Application([(r"/", MainHandler), (r"/widget/", WidgetHandler), (r"/widget/(?P<pid>\w+)", WidgetHandler)])


if __name__ == "__main__":
    app = MainHandler.make_app()
    app.listen(8888)    # Port Number
    tornado.ioloop.IOLoop.current().start()
