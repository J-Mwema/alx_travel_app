# ALX Travel App

This repository is an early Django foundation for a travel listings API. The
current listing endpoint is a placeholder response; this checkout does not
yet implement listing or booking CRUD, authentication flows, or background
jobs.

## Current accomplishments

- Django project configuration with a MySQL database connection.
- A `listings` app mounted at `/listings/`.
- Swagger and ReDoc routes for API exploration.
- A placeholder listings response to verify that the route is reachable.

## Project map

| Path | Purpose |
| --- | --- |
| [`alx_travel_app/`](alx_travel_app/README.md) | Django entry point, project package, and app modules |
| [`alx_travel_app/manage.py`](alx_travel_app/manage.py) | Django management command entry point |
| [`alx_travel_app/alx_travel_app/`](alx_travel_app/alx_travel_app/) | Settings, root URLs, and WSGI/ASGI configuration |
| [`alx_travel_app/alx_travel_app/listings/`](alx_travel_app/alx_travel_app/listings/) | Listings URL, view, model placeholder, and tests |
| [`alx_travel_app/alx_travel_app/requirement.txt`](alx_travel_app/alx_travel_app/requirement.txt) | Python dependencies |

## Local setup

Python 3.8+ and a MySQL server are required. From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r alx_travel_app/alx_travel_app/requirement.txt
```

Create a local `.env` file next to `manage.py` with `SECRET_KEY`, `DB_NAME`,
`DB_USER`, and `DB_PASSWORD`; optionally set `DEBUG`, `DB_HOST`, and `DB_PORT`.
Create the corresponding MySQL database, then run:

```bash
cd alx_travel_app
python3 manage.py migrate
python3 manage.py runserver
```

The API placeholder is at `/listings/`; the generated docs are at `/swagger/`
and `/redoc/`. See the [Django project guide](alx_travel_app/README.md) for
links to its app and configuration files.
