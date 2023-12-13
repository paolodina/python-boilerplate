"""Docstring"""
import pkg_resources
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from {{ python_package_name }}.common.main import hello_world

app = FastAPI(
    title="{{ project_name }} API",
    version=pkg_resources.get_distribution("{{ python_package_name }}").version,
)


@app.get("/")
async def root() -> RedirectResponse:
    """Redirect to docs."""
    return RedirectResponse("/docs")


@app.post(
    "/hello",
)
async def hello() -> str:
    """Hello"""
    return hello_world()
