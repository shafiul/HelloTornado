import logging
from sqlalchemy import Column, Integer, String
import models.base
from models.base import Result


class User(models.base.Base.instance().get_base()):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50), unique=True)
    group = Column(Integer)
    password = Column(String(50))

    logger = logging.getLogger(__name__)

    def add_user(self):
        result = Result()

        session = None
        try:
            session = models.base.Base.instance().get_session()
            session.add(self)
            #commit
            session.commit()
        except Exception as e:
            self.logger.fatal('Exception while user registration: {0}'.format(e))
            session.rollback()
            result.set_result(result.RESULT_TYPE_DB_ERR, [{'db': 'Undefined error'}])
        finally:
            pass

        return result