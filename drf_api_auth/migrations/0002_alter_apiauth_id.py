# Generated by Django 4.2.13 on 2024-06-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_auth", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apiauth",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
