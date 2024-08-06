import logging
import sys

logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
logging.getLogger().setLevel(logging.DEBUG)

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler("{0}.log".format("outliers.log"))
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

# logging.basicConfig(filename='outliers.log',
#                     level=logging.DEBUG,
#                     format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

logging.debug('Message to help debug ...')
logging.info('General info about a process that is running ...')
logging.warning('Warn, but no need to error ...')