# import Patients.src.backend_models.db_connection as m
# from Patients.src.backend_models import db_connection
from Patients.src.backend_models.db_connection import connection
from Patients.src.frontend_views.template import frontend_template
from Patients.src.controller_controllers.middleware import mvc_middleware
import numpy, pytest_bdd
import logging, argparse

from logging.handlers import TimedRotatingFileHandler

if __name__ == '__main__':
    #argparse configuration
    parser = argparse.ArgumentParser()
    requiredNamed = parser.add_argument_group("Required named argument")
    requiredNamed.add_argument('-e', '--email_id', dest = 'email_id',
                               help='please enter the email address', required=True, nargs='+')
    args = parser.parse_args()
    email_address = args.email_id


    # Logging Configuration
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(lineno)d %(message)s', datefmt = '%Y-%m-%d--%H:%M:%S')
    fileHandler = logging.FileHandler(filename= r'C:\Users\prema\PycharmProjects\HospitalApplications\Patients\log\app.log')
    fileHandler.setFormatter(formatter)

    # logname = r'C:\Users\prema\PycharmProjects\HospitalApplications\Patients\log\app.log'
    # handler = TimedRotatingFileHandler(logname, when="midnight", interval=1)
    # handler.suffix = "%Y%m%d"
    # logger.addHandler(handler)

    # logger.setLevel(level = logging.DEBUG)
    logger.setLevel(level=logging.DEBUG)
    logger.addHandler(fileHandler)

    streamhandler = logging.StreamHandler()
    streamhandler.setLevel(logging.CRITICAL)
    streamhandler.setFormatter(formatter)
    logger.addHandler(streamhandler)


    logger.debug("Starting...")

    logger.debug("Call to connection method...")

    connection()
    frontend_template()
    mvc_middleware()

    logger.info("Email address - {}".format(email_address))

    logger.critical("General Error")
