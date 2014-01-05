from tornado.web import RequestHandler
from modules.user import UserActions


class UserRegistrationHandler(RequestHandler):

    def get(self):
        UserActions.UserRegistrationExecutor(self)