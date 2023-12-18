"""Docstring"""
import typer
from typing_extensions import Annotated

from {{ python_package_name }}.api.something import a_cool_function
from {{ python_package_name }}.common.utils import get_logger

logger = get_logger(__name__)
cli = typer.Typer(add_completion=False)


@cli.command()
def hello_world(
        name: Annotated[str, typer.Option(help="Your name.")] = "cowboy"
) -> str:
    """Hello."""
    a_cool_function()
    logger.info(f"We are here, {name}")
    return f"We are here, {name}"


if __name__ == '__main__':
    cli()
