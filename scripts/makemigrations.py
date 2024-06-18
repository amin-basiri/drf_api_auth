"""A stand-alone equivalent of `python manage.py makemigrations`."""
import pathlib
import sys

import django
from django.core.management import call_command

root = pathlib.Path(__file__).parent.parent
sys.path.append(str(root))

if __name__ == "__main__":
    from django.conf import settings

    settings.configure(
        SECRET_KEY="secret",
        INSTALLED_APPS=(
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.sites",
            "django.contrib.staticfiles",
            "rest_framework",
            "drf_api_auth",
        ),
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
    )

    django.setup()

    app_labels = [
        "api_auth",
    ]
    call_command("makemigrations", *app_labels)
