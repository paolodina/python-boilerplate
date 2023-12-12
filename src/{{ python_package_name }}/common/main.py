"""Docstring"""
from {{ python_package_name }}.api.something import a_cool_function
from {{ python_package_name }}.common.utils import get_logger

logger = get_logger(__name__)


def hello_world() -> str:
    """Hello."""
    a_cool_function()
    logger.info("We are here")
    return "We are here"
