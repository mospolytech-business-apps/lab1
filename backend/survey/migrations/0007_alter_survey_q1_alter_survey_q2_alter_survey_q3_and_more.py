# Generated by Django 4.2.5 on 2023-10-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_alter_survey_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='q1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='q2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='q3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='q4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]