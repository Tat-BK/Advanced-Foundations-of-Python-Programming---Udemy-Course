import logging

# Building and configuring the logger
logging.basicConfig(filename="main.log",
                    format = "%(asctime)s %(message)s",
                    filemode = "w") # "write or append"

# setting an object for the logger
mylogger = logging.getLogger()

# setting the threshold to debug
mylogger.setLevel(logging.DEBUG)

# Testing Messages for that Log
mylogger.debug("This is a harmless debug message")
mylogger.info("Information Message")
mylogger.warning("This is a warning message")
mylogger.error("This is an error message")
mylogger.critical("No internet, Internet is down")
