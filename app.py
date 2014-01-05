import logging
import logging.config
import tornado.web
import tornado.ioloop
from models.base import Base
from modules.user.handlers import UserRegistrationHandler
import modules.user.routes

application = tornado.web.Application(
    modules.user.routes.routes
)

if __name__ == '__main__':
    # Configure Logging
    logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
    # Start application

    logger = logging.getLogger(__name__)
    # Create database
    Base.instance().create_tables()
    logger.debug( "Starting application..." )
    application.listen(8888)
    logger.debug('started listening to port.')
    tornado.ioloop.IOLoop.instance().start()
    logger.debug( 'IO loop has started' )