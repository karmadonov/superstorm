import logging
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options, parse_config_file


define("settings", type=str, help="Path to config file",
       callback=lambda path: parse_config_file(path, final=False))
define("port", default=8088, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def main():
    tornado.options.parse_config_file('settings/base.conf')
    tornado.options.parse_command_line()

    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    logging.info('Running Tornado on 127.0.0.1:%s', options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
