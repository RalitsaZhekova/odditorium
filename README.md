# Odditorium

## Run locally

Install Python 3.13. Download and extract the project, then open a terminal in the folder containing `manage.py`.

### Windows (PowerShell)

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

### macOS / Linux

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python manage.py migrate
.venv/bin/python manage.py runserver
```

Open http://127.0.0.1:8000/.

No environment variables or credentials are required. The default settings use SQLite, and migrations create the local database.

## Verify the custom 404 page

Django shows its technical error page when `DEBUG=True`. To see Odditorium’s
custom 404 page, stop the development server and restart it with debugging
disabled.

**Windows PowerShell**

```powershell
$env:DJANGO_DEBUG = "False"
python manage.py runserver --insecure
```

**macOS or Linux**

```bash
DJANGO_DEBUG=False python manage.py runserver --insecure
```

Open http://127.0.0.1:8000/missing-exhibit/. The custom page should appear,
and the server log should show HTTP `404`. The `--insecure` flag serves
the stylesheet during this local check.

After stopping the server in PowerShell, clear the temporary override
before starting it normally again:

```powershell
Remove-Item Env:DJANGO_DEBUG
```
