"""Logging utilities."""
import logging
import os
import sys
from datetime import datetime


def get_logger(name: str) -> logging.Logger:
    """Generate logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    os.makedirs("log", exist_ok=True)
    # file handler
    fh = logging.FileHandler(f"log/{{ python_package_name }}.{datetime.now().date()}.log")
    fh.setLevel(level=logging.DEBUG)
    # console handler
    sh = logging.StreamHandler(sys.stderr)
    fh.setLevel(level=logging.INFO)
    # formatter
    formatter = logging.Formatter(
        "[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
    )
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    # add handlers
    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger
