# Odditorium

A museum of wonderfully useless inventions, built with Django templates and SQLite.

This first increment provides the project setup and a landing page. Domain models and CRUD features will follow in separate commits.

## Requirements

- Python 3.13 or newer supported by the pinned Django version
- Git
- VS Code with the recommended Python extensions (optional)

## Local setup in Windows PowerShell

Open this folder in VS Code, then open its terminal:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

If PowerShell blocks activation, use `.\.venv\Scripts\python.exe` instead of `python` in the commands above; activation is optional.

## Local setup in macOS or Linux

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000/. In VS Code, use **Python: Select Interpreter** to select the interpreter inside `.venv`. The included launch configuration supports F5 debugging.

## Environment configuration

No environment variables or credentials are required for local evaluation. SQLite, local hosts, and development settings work by default. Optionally copy `.env.example` to `.env` and edit it:

| Variable | Default | Purpose |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Development-only fallback | Local signing key; use a private random key for deployment |
| `DJANGO_DEBUG` | `True` | Set to `False` outside local development |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1,[::1]` | Comma-separated allowed hostnames |

Existing process environment variables take precedence over `.env`. Never commit `.env`. Production deployment is outside this increment.

## Project structure

- `config`: settings and root URL configuration
- `common`: homepage and shared UI
- `galleries`: planned collection management; avoids shadowing Python's `collections` module
- `inventions`: planned invention catalogue
- `tours`: planned themed tours
- `templates`: Django templates and reusable partials
- `static`: local CSS and future assets

No authentication, seed data, or admin workflow is implemented. All domain objects will be created through the public UI in subsequent increments.

## Checks

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
```

## Local Git workflow

If you extracted the supplied archive, its `.git` directory contains the initial commit. Open this folder itself, rather than its parent. Set your identity before future commits:

```bash
git config user.name "Your Name"
git config user.email "your-verified-github-email@example.com"
git log --oneline
git status
```

The prepared initial commit is attributed to Codex. If you want to take authorship of this initial setup after reviewing it, set your identity and run `git commit --amend --reset-author --no-edit` before sharing the repository.

For each completed increment:

```bash
git add .
git diff --cached
git commit -m "Describe the completed change"
```

The virtual environment, `.env`, database, caches, and uploads are ignored. Migrations, dependencies, `.env.example`, and shared VS Code configuration are tracked. The exam requires actual commits on at least five separate days.

## Push to GitHub later

Create an **empty** public GitHub repository: do not initialize it with a README, license, or gitignore. Then run:

```bash
git remote add origin https://github.com/YOUR_USERNAME/odditorium.git
git push -u origin main
```

Pushing transfers existing commits and their dates and authors. It preserves local history. The archive must retain `.git`; copying source files alone does not preserve commits. Do not run `git init` in a different folder and expect it to contain this history.
