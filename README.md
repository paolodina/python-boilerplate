# Python Projects Template

Special thanks:

- <https://github.com/massimo-lu/boilerplate>
- <https://github.com/duarteocarmo/boilerplate>
  - <https://duarteocarmo.com/blog/opinionated-python-boilerplate>

## ✨ Quick start

To create a new project from this template, simply run:

```shell
pip install copier
copier copy -r devel https://github.com/paolodina/python-boilerplate path/to/destination
```

or

```bash
pipx run copier copy -r devel https://github.com/paolodina/python-boilerplate path/to/destination
```

Answer the prompt questions and enjoy!

### 📐 Design choices

- [Hatchling](https://hatch.pypa.io/latest/) build system
- [Ruff](https://docs.astral.sh/ruff/) formatting
- [Mypy](https://mypy.readthedocs.io/en/stable/) type checking
- [Pre-commit](https://pre-commit.com/) hooks to enforce Ruff and Mypy checks
- [Pdoc](https://pdoc.dev/) documentation
- [Typer](https://typer.tiangolo.com/) command-line interface
- [FastAPI](https://fastapi.tiangolo.com/) API
