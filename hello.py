import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import time

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")


class PringHttpHeader(tornado.web.RequestHandler):
    def get(self):
        self.write(self.request.method)
        self.write(self.request.headers)


class Logtest(tornado.web.RequestHandler):
    def get(self):
        filename = self.get_argument("file")
        i = 0
        while i < 100:
            f = open(filename, 'a')
            f.write(str(i))
            i += 1
            print i
            f.close()
            time.sleep(3)


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/http-header/", PringHttpHeader),
        (r"/log-test", Logtest),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
