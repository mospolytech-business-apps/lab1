# Generated by Django 4.2.5 on 2023-12-02 03:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0008_user_is_new_alter_user_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                blank=True, default=False, verbose_name="Активность"
            ),
        ),
    ]
