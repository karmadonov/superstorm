import logging
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

from superstorm.conf import get_settings
from superstorm.handlers import MainHandler


define('settings', type=str, help='Path to config file',
       default='settings/prod.json')
define('port', default=80, help='Run on the given port', type=int)


def main():
    tornado.options.parse_command_line()

    installed_handlers = (MainHandler, )
    handlers, settings = get_settings(options.settings, installed_handlers)

    application = tornado.web.Application(handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    logging.info('Running Tornado on 127.0.0.1:%s', settings['port'])
    http_server.listen(settings['port'])
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
