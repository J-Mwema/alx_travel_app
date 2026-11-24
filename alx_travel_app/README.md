# Travel app Django project

[Back to the repository overview](../README.md)

This directory contains the Django command-line entry point and project
package. The `/listings/` route currently returns a placeholder response.

## Project files

- [`manage.py`](manage.py) — run Django commands from this directory.
- [`alx_travel_app/`](alx_travel_app/) — settings, URL configuration, and
  WSGI/ASGI entry points.
- [`alx_travel_app/listings/`](alx_travel_app/listings/) — the listings
  endpoint, model placeholder, and tests.
- [`alx_travel_app/requirement.txt`](alx_travel_app/requirement.txt) —
  pinned Python dependencies.

## Run

Install dependencies and configure the local environment using the
[root setup guide](../README.md#local-setup). SQLite is the default database;
MySQL can be selected with environment variables. Copy the repository's
`.env.example` to `.env`, then run from this directory:

```bash
python3 manage.py migrate
python3 manage.py runserver
```

The API is available locally at `http://127.0.0.1:8000/listings/`; API
documentation is available at `/swagger/` and `/redoc/`. There is no live
deployment at this time. See the [repository overview](../README.md) for
current scope and setup instructions.
