import logging
import asyncio

# Init logging
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO)


async def startup():
    logging.info("InMemory cache initiated")
    await get_service_handlers()
    logging.info("Updated global service handlers")


async def get_service_handlers():
    handlers = {'mlflow': mlflow_handler}
    logging.info("Retreving mlflow handler {}".format(mlflow_handler))
    return handlers


def mlflow_handler():
    logging.info("test")


asyncio.run(startup())
