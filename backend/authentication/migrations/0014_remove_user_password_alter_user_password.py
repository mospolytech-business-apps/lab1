# Generated by Django 4.2.1 on 2023-11-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0013_user_password"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="Password",
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=255),
        ),
    ]
