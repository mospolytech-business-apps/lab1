# Generated by Django 4.2.5 on 2023-10-13 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0002_remove_role_role_id'),
        ('authentication', '0005_user_office'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='role.role'),
        ),
    ]
