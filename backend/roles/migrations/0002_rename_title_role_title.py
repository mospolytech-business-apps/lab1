# Generated by Django 4.2.1 on 2023-11-11 17:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("roles", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="role",
            old_name="title",
            new_name="Title",
        ),
    ]