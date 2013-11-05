import tornado.auth
import tornado.escape

from tornado import gen


from superstorm.handlers import BaseHandler


class AuthHandler(BaseHandler, tornado.auth.GoogleMixin):

    url = r'/auth/login'

    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        if self.get_argument("openid.mode", None):
            user = yield self.get_authenticated_user()
            self.set_secure_cookie("user", tornado.escape.json_encode(user))
            self.redirect("/")
            return
        self.authenticate_redirect()


class LogoutHandler(BaseHandler):

    url = r'/auth/logout'

    def get(self):
        self.clear_cookie("user")
        self.write('You are now logged out. '
                   'Click <a href="/">here</a> to log back in.')


class UserHandler(BaseHandler):

    url = r'/auth/user'

    def get(self):
        user = self.get_current_user()
        self.write(tornado.escape.json_encode(user) if user else '')
