from tornado.web import RequestHandler
from modules.user import UserActions

__author__ = 'shantanu'


class UserRegistrationHandler(RequestHandler):

    def get(self):
        result = UserActions.UserRegistrationExecutor(self)
        self.write({ 'id': result.id })
        # self.write("hello world")