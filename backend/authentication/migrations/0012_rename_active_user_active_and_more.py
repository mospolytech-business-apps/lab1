# Generated by Django 4.2.1 on 2023-11-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0011_rename_is_active_user_active_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="active",
            new_name="Active",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="birthday",
            new_name="Birthday",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="email",
            new_name="Email",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="firstname",
            new_name="FirstName",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="lastname",
            new_name="LastName",
        ),
        migrations.AddField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]