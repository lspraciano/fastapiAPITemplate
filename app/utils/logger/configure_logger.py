import logging
import sys


def configure_logger() -> logging.Logger:
    logger: logging.Logger = logging.getLogger(
        name=__name__
    )
    logger.setLevel(
        level=logging.INFO
    )
    console_formatter: logging.Formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(message)s"
    )
    console_handler: logging.StreamHandler = logging.StreamHandler(
        stream=sys.stdout
    )
    console_handler.setFormatter(
        fmt=console_formatter
    )
    logger.addHandler(
        hdlr=console_handler
    )

    return logger
