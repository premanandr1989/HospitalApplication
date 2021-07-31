import logging

logger = logging.getLogger(__name__)

def connection():
    logger.info("DB Connection switching on")

if __name__ == '__main__':
    print("DB Connection Module")
    connection()
