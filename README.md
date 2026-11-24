# ALX Travel App

ALX Travel App is an early-stage Django project that exposes a placeholder
travel listings API. It includes a Django REST Framework setup, API schema
documentation, and a basic test for the listings endpoint. It does not yet
provide listing or booking management, authentication, or a hosted demo.

## Current API

| Route | Purpose |
| --- | --- |
| `/listings/` | Placeholder response confirming the endpoint is reachable |
| `/swagger/` | Swagger API documentation |
| `/redoc/` | ReDoc API documentation |

## Local setup

Python 3.8+ is required. Create and activate a virtual environment, then
install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r alx_travel_app/alx_travel_app/requirement.txt
```

Copy `.env.example` to `.env` and set a local `SECRET_KEY`. SQLite is used by
default. To use MySQL instead, set `DB_ENGINE=mysql` and configure `DB_NAME`,
`DB_USER`, and `DB_PASSWORD` (optionally `DB_HOST` and `DB_PORT`).

Start the app from the Django project directory:

```bash
cd alx_travel_app
python3 manage.py migrate
python3 manage.py runserver
```

Open `http://127.0.0.1:8000/listings/` or the local documentation routes
listed above. There is currently no live deployment URL.

## Checks and tests

```bash
cd alx_travel_app
python3 manage.py check
python3 manage.py test
```

GitHub Actions runs these Django checks and tests on pushes and pull requests.

## Project layout

- [`alx_travel_app/`](alx_travel_app/README.md) — Django command-line entry
  point, project configuration, and app modules.
- [`alx_travel_app/alx_travel_app/listings/`](alx_travel_app/alx_travel_app/listings/)
  — listings route, placeholder view/model, and test.
- [`alx_travel_app/alx_travel_app/requirement.txt`](alx_travel_app/alx_travel_app/requirement.txt)
  — pinned Python dependencies.
