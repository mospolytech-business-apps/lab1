# Generated by Django 4.2.1 on 2023-11-11 17:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0003_rename_booking_reference_ticket_bookingreference_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ticket",
            old_name="bookingreference",
            new_name="BookingReference",
        ),
        migrations.RenameField(
            model_name="ticket",
            old_name="confirmed",
            new_name="Confirmed",
        ),
        migrations.RenameField(
            model_name="ticket",
            old_name="email",
            new_name="Email",
        ),
        migrations.RenameField(
            model_name="ticket",
            old_name="firstname",
            new_name="FirstName",
        ),
        migrations.RenameField(
            model_name="ticket",
            old_name="lastname",
            new_name="LastName",
        ),
        migrations.RenameField(
            model_name="ticket",
            old_name="passportnumber",
            new_name="PassportNumber",
        ),
        migrations.RenameField(
            model_name="ticket",
            old_name="phone",
            new_name="Phone",
        ),
    ]
