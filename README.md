# {{ project_name }}

To create a new project from this template:
```shell
pip install copier
copier copy . path/to/destination
```

## Development

* Make sure you are running in a virtual environment (e.g., `python3 -m venv .env`)
* Activate it (e.g. `source .env/bin/activate`)
```shell
(.env) $ make install-dev
```

* Run the tests:
```shell
(.env) $ make test
```

* Run code checks:
```shell
(.env) $ make check
```

* For more help:
```shell
(.env) $ make help
```
