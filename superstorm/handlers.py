import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    def get_login_url(self):
        return u"/login"

    def get_current_user(self):
        user_json = self.get_secure_cookie('user')
        return tornado.escape.json_decode(user_json) if user_json else None


class MainHandler(BaseHandler):

    url = r'/'

    def get(self):
        self.render('base.html')
