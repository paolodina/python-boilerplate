# Python Projects Template

Special thanks:

- <https://github.com/massimo-lu/boilerplate>
- <https://github.com/duarteocarmo/boilerplate>
  - <https://duarteocarmo.com/blog/opinionated-python-boilerplate>

## ✨ Quick start

Create a new project called `myproject`.

### pip version

To create a new project from this template, simply run:

```shell
$ pwd
/home/user/devel/myproject
$ python -m venv .venv
$ . .venv/bin/activate
pip install -U pip copier
copier copy -r devel https://github.com/paolodina/python-boilerplate .
# Answer the questions, project name: myproject
$ git init && git add . && git commit -m 'first commit'
$ make install-dev
# ...wait...
$ myproject
[03/17/24 15:48:27] INFO     Hello, World   main.py:16
```

### pipx version

To create a new project from this template, simply run:

```bash
$ pwd
/home/user/devel
$ pipx run copier copy -r devel https://github.com/paolodina/python-boilerplate myproject
# Answer the questions, project name: myproject
$ cd myproject
$ git init && git add . && git commit -m 'first commit'
$ python -m venv .venv
$ . .venv/bin/activate
$ make install-dev
# ...wait...
$ myproject
[03/17/24 15:48:27] INFO     Hello, World   main.py:16
```

Enjoy!

### 📐 Design choices

- [Hatchling](https://hatch.pypa.io/latest/) build system
- [Ruff](https://docs.astral.sh/ruff/) formatting
- [Mypy](https://mypy.readthedocs.io/en/stable/) type checking
- [Pre-commit](https://pre-commit.com/) hooks to enforce Ruff and Mypy checks
- [Pdoc](https://pdoc.dev/) documentation
- [Typer](https://typer.tiangolo.com/) command-line interface
- [FastAPI](https://fastapi.tiangolo.com/) API
