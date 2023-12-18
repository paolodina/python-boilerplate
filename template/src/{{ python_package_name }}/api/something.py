"""Docstring"""
from {{ python_package_name }}.common.utils import get_logger

logger = get_logger(__name__)


def a_cool_function() -> str:
    """Very cool."""
    logger.info("We are here")
    return "We are here"
