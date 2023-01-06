import logging
import os
from functools import wraps

logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s")
logger = logging.getLogger("Decorators")
logger.setLevel(os.environ.get("LOGGING", logging.DEBUG))


def notify_cloudwatch(function):
    """Print Lambda incoming event and output result to logs."""

    @wraps(function)
    def wrapper(event, context):
        logger.info(f"'{context.function_name}' - entry.\nIncoming event: '{event}'")
        result = function(event, context)
        logger.info(f"'{context.function_name}' - exit.\nResult: '{result}'")
        return result

    return wrapper
