from modules.user.handlers import UserRegistrationHandler

__author__ = 'shantanu'
routes = [
    (r'/user/add/?', UserRegistrationHandler),
]