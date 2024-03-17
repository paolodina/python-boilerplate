# {{ project_name }}

{{ project_description }}

## Quick start

Install the package

```shell
make install
```

Run through the CLI:

```shell
{{ python_package_name }} --help
```

Or start the API:

```shell
make api
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
