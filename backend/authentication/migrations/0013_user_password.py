# Generated by Django 4.2.1 on 2023-11-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0012_rename_active_user_active_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="Password",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
