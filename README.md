# Keep Account — Django Bookkeeping Demo

A historical Django web application for recording income and expenses, reviewing spending by category, and tracking an asset balance and expected spending. The project is retained as an example of an early full-stack application with forms, authentication, charts, and CSV export.

> **Project status:** This is a historical learning project and is no longer actively maintained. It is intended for local demonstration and code review. Production deployment and ongoing production support are outside its maintained scope.

## Features

- User registration, login, and logout.
- Create, update, delete, and search bookkeeping entries.
- Record the date, category, description, and amount for each entry.
- Display category totals with pie and bar charts.
- Review monthly income, spending, balance, and remaining planned spending.
- Track an asset balance and expected spending.
- Export recorded entries as CSV.

## Demo video

Watch the original project demonstration: https://www.youtube.com/watch?v=DrLOVDgh7vY&ab_channel=ChuOkumo

## Project structure

| Path | Purpose |
| --- | --- |
| `homework/` | Django project configuration and top-level routing |
| `keepAccount/` | Bookkeeping models, forms, views, templates, and migrations |
| `users/` | Registration and authentication views and templates |
| `manage.py` | Django management-command entry point |
| `requirements.txt` | Original pinned Python dependencies |
| `staticfiles/` | Collected third-party Django admin assets |

## Original environment

The recorded application uses Django 4.1.3, with Python 3.10.7 indicated in `runtime.txt`. The dependency file also pins Gunicorn, Pillow, asgiref, and sqlparse. Bootstrap and Chart.js are loaded from external CDNs in the templates.

These versions document the original implementation. They are not a guarantee that a fresh environment or deployment will work without further updates.

## Local demonstration

1. Clone the repository and create a Python virtual environment compatible with the recorded dependencies.
2. Activate the environment and install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Configure a fresh local SQLite database and your own local development settings. The repository includes historical settings and a database file; their presence is not a claim that they are suitable for deployment or contain approved sample data.
4. Initialize the local database:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open the local address printed by Django, register an account, and add demonstration entries.

This documentation and language refresh did not execute the application against the committed database or validate a live deployment.

## Language and data compatibility

Category selection labels, transaction tables, and chart labels are displayed in English. The stored category codes remain unchanged so existing records and income/expense calculations retain their original meaning. CSV exports also retain those stored codes. The new category-label migration updates model metadata without translating existing financial data.

Historical migrations, user-entered descriptions, the original demo video, and third-party assets remain in their original form. The database and deployment settings are not modified by this language refresh.
