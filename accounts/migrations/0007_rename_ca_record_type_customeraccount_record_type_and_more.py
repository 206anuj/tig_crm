# Generated by Django 4.2 on 2024-07-08 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_va_phone_number_vendoraccount_va_primary_contact_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeraccount',
            old_name='ca_record_type',
            new_name='record_type',
        ),
        migrations.RenameField(
            model_name='vendoraccount',
            old_name='va_record_type',
            new_name='record_type',
        ),
    ]
