# Travel app Django project

[Back to the repository overview](../README.md)

This directory contains the Django command-line entry point and project
package for the travel listings API.

## Project files

- [`manage.py`](manage.py) — run Django commands from this directory.
- [`alx_travel_app/`](alx_travel_app/) — settings, URL configuration, and
  WSGI/ASGI entry points.
- [`alx_travel_app/listings/`](alx_travel_app/listings/) — the listings
  endpoint, model placeholder, and tests.
- [`alx_travel_app/requirement.txt`](alx_travel_app/requirement.txt) —
  pinned Python dependencies.

## Run

Install dependencies and configure the local MySQL environment using the
[root setup guide](../README.md#local-setup). From this directory:

```bash
python3 manage.py migrate
python3 manage.py runserver
```

The listings route currently returns a placeholder response. The repository
root describes the [implemented scope and available API routes](../README.md).
