# Generated by Django 4.2.1 on 2023-11-11 17:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0010_rename_office_user_officeid_rename_role_user_roleid"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="is_active",
            new_name="active",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="first_name",
            new_name="firstname",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="last_name",
            new_name="lastname",
        ),
    ]
