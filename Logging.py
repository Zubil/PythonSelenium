import logging

logging.basicConfig(filename="C:/logs/my.log",
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG
                   )

logging.debug("This is Debug message")
logging.info("This is info message")
logging.error("This is error message")
logging.warning("This is warning message")
logging.critical("This is critical message")