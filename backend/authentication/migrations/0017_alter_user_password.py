# Generated by Django 4.2.1 on 2023-11-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0016_alter_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=255),
        ),
    ]
