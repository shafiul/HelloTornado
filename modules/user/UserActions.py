import logging
from tornado.web import RequestHandler
from models.base import Base
from models.user import User


class UserRegistrationExecutor():

    def __init__(self, handler):
        """
            @type handler: RequestHandler
        """
        self._handler = handler
        self.id = 0
        self.logger = logging.getLogger(__name__)
        self.do_action()

    def do_action(self):
        self.logger.debug('Inside do action');
        params = {
            'username': self._handler.get_argument('username'),
            'firstname': self._handler.get_argument('firstname'),
            'lastname': self._handler.get_argument('lastname'),
            'email': self._handler.get_argument('email'),
            'group': self._handler.get_argument('type'),
            'password': '',
        }

        self.logger.debug('now calling model')

        # validation_errors = self._validate(params)
        #
        # if validation_errors != None:
        #     pass

        # make model
        new_user = User(**params)
        session = (Base.instance().get_session())()
        session.add(new_user)
        #commit
        session.commit()

        user_id = new_user.id
        # Log this output?
        self.id = user_id

        # remove session
        (Base.instance().get_session()).remove()
        # def _validate(self, params):
    #     return None