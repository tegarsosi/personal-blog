# 🖋️ The Inked Paper
**A private, minimalist journal built with FastAPI, Postgres & Tailwind CSS.**

A project from [roadmap.sh](https://roadmap.sh/projects/personal-blog)

The Inked Paper is a minimalist personal journal for developers who like monochrome design and simple architecture. Every page sits behind a login, so only the author can read and write entries.

## ✨ Key Features
* **Private by Default**: Every page (home, articles, admin) requires login. Visitors who aren't logged in are redirected to `/login`.
* **Custom Login Page**: Session-based authentication with a signed cookie (Starlette `SessionMiddleware` + `itsdangerous`). No browser popup.
* **Full CRUD**: Create, read, update and delete entries from the admin dashboard.
* **Postgres Storage**: Entries are stored in a database through [SQLModel](https://sqlmodel.tiangolo.com/). Local development uses SQLite; production uses [Neon](https://neon.tech) Postgres.
* **Serverless Deployment**: Runs on [Vercel](https://vercel.com).
* **Ink-Ready UI**: A "Bento-style" interface inspired by minimalist print design, built with Tailwind CSS.

## 🛠️ Tech Stack
* **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python 3.14)
* **Database / ORM**: [SQLModel](https://sqlmodel.tiangolo.com/), SQLite (local) & Postgres on [Neon](https://neon.tech) (production)
* **Auth**: Signed session cookies via Starlette `SessionMiddleware`
* **Frontend**: [Jinja2 Templates](https://jinja.palletsprojects.com/) & [Tailwind CSS](https://tailwindcss.com/)
* **Hosting**: [Vercel](https://vercel.com)
* **Dependency Management**: [uv](https://github.com/astral-sh/uv)

## 📁 Project Structure
```
main.py            # App entry point: middleware, startup, reader routes
db.py              # Database engine; reads DATABASE_URL (falls back to SQLite)
models.py          # Article table (SQLModel)
services.py        # BlogService: all database reads and writes
dependencies.py    # Credential check + require_login guard
routers/
  auth.py          # /login and /logout
  admin.py         # /admin dashboard: add, edit, delete
templates/         # Jinja2 pages
static/            # CSS
import_json.py     # One-off migration from the old JSON files into the database
```

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.14
* [uv](https://github.com/astral-sh/uv)

### 2. Installation
```bash
git clone https://github.com/tegarsosi/personal-blog.git
cd personal-blog
uv sync
```

### 3. Environment Variables
Copy the example file and fill in your values:
```bash
cp .env.example .env
```

| Variable | Required | Description |
|---|---|---|
| `ADMIN_USERNAME` | Yes | Username for the login page |
| `ADMIN_PASSWORD` | Yes | Password for the login page. Use a long, random one. |
| `SECRET_KEY` | Yes | Signs the session cookie. The app won't start without it. |
| `DATABASE_URL` | No (locally) | Postgres connection string. If it's not set, the app uses a local `blog.db` SQLite file. |

Generate a `SECRET_KEY` with:
```bash
uv run python -c "import secrets; print(secrets.token_urlsafe(32))"
```

> Only add `DATABASE_URL` once you have a real value. An empty or invalid value makes the app fail to start.

### 4. Run Locally
```bash
uv run uvicorn main:app --reload
```
Open http://localhost:8000. You'll be redirected to `/login`.
