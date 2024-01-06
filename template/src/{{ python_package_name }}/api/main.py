"""Docstring"""
from importlib.metadata import metadata, version

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field

from {{ python_package_name }}.common.main import hello_world

app = FastAPI(
    title="{{ project_name }} API",
    version=version("{{ python_package_name }}"),
    summary=metadata("{{ python_package_name }}")["Summary"],
)


class Hello(BaseModel):
    """Request schema for /hello endpoint."""

    name: str = Field(default="World", description="Your name.")


@app.get("/")
async def root() -> RedirectResponse:
    """Redirect to docs."""
    return RedirectResponse("/docs")


@app.post(
    "/hello",
)
async def hello(request: Hello) -> str:
    """Hello"""
    return hello_world(request.name)
