# Generated by Django 3.0 on 2022-10-27 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_lettings", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name_plural": "addresses"},
        ),
    ]
