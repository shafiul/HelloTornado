import logging
import logging.config
import tornado.web
import tornado.ioloop
from models.base import Base
import modules.user.routes

application = tornado.web.Application(
    modules.user.routes.routes
)

if __name__ == '__main__':
    # Configure Logging
    logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    # Create database
    Base.instance().create_tables()
    logger.debug( "Starting application..." )
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()