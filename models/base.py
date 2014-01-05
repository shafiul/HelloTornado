import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


class Base():
    def __init__(self):
        self._engine = create_engine('mysql+pymysql://root:root@localhost/shafiul', echo=True)
        session_factory = sessionmaker(bind=self._engine)
        self._Session = scoped_session(session_factory)
        self._Base = declarative_base()
        self.logger = logging.getLogger(__name__)
        self.logger.info('Database initialized.')

    @classmethod
    def instance(cls):
        """Singleton like accessor to instantiate backend object"""
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def get_base(self):
        return self._Base

    def get_session(self):
        return self._Session()

    def create_tables(self):
        self.logger.info('Creating database...')
        self._Base.metadata.create_all(self._engine)

    def remove(self):
        self._Session.remove()


class Result():

    RESULT_TYPE_SUCCESSFUL = 1
    RESULT_TYPE_DB_ERR = 0
    RESULT_TYPE_VALIDATION_ERR = -1

    def __init__(self):
        self._type = self.RESULT_TYPE_SUCCESSFUL
        self._errors = None

    def set_result(self, type, errors):
        self._type = type
        self._errors = errors

    def is_successful(self):
        return self._type == self.RESULT_TYPE_SUCCESSFUL

    def get_errors(self):
        return self._errors

    def get_type(self):
        return self._type