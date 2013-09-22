import json

import tornado.web


def load_from_file(file_name):
    """ Read json files by `file_name` and return dict object.
    """
    with open(file_name) as settings:
        return json.load(settings)


def get_settings(settings_file_name, installed_handlers):
    """ Generate settings for tornado.web.Application from json configs.

        Required parameters:
            settings_file_name -- name of file with users settings
            installed_handlers -- list of installed handlers.
    """
    settings = load_from_file('settings/base.json')
    settings.update(load_from_file(settings_file_name))
    handlers = [(r"/static/(.*)", tornado.web.StaticFileHandler,
                 {"path": settings['static_path']})]
    handlers = [(handler.url, handler) for handler in installed_handlers]
    return handlers, settings
