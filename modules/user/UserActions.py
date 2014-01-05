import logging
from tornado.web import RequestHandler, HTTPError
import models
from models.base import Base
from models.user import User
from util.output import OutputUtil


class UserRegistrationExecutor():

    def __init__(self, handler):
        """
            @type handler: RequestHandler
        """
        self._handler = handler
        self.logger = logging.getLogger(__name__)
        self.do_action()

    def do_action(self):
        self.logger.debug('Inside do action')

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

        try:
            new_user = User(**params)
            result = new_user.add_user()

            # Prepare response
            response = {
                'status': OutputUtil.TYPE_SUCCESSFUL,
                'errors': [],
                'userid': 0,
            }

            if result.is_successful():
                response['userid'] = new_user.id
            else:
                response['status'] = result.get_type()
                response['errors'] = result.get_errors()

            # generate output

            self._handler.write(response)
        except Exception as e:
            self.logger.error('Error in add user action: {0}'.format(e))
            raise HTTPError(500)
        finally:
             # remove session
            models.base.Base.instance().remove()


        # def _validate(self, params):
    #     return None