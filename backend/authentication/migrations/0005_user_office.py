# Generated by Django 4.2.5 on 2023-10-06 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0004_remove_office_user_id'),
        ('authentication', '0004_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='office.office'),
        ),
    ]
