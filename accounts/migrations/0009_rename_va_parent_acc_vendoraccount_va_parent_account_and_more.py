# Generated by Django 4.2 on 2024-07-08 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_rename_va_phone_no_vendoraccount_va_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendoraccount',
            old_name='va_parent_acc',
            new_name='va_parent_account',
        ),
        migrations.AlterField(
            model_name='vendoraccount',
            name='va_bank_accept_euro',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vendoraccount',
            name='va_bank_accept_usd',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vendoraccount',
            name='va_company_24x7_support',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vendoraccount',
            name='va_multilingual_helpdesk',
            field=models.BooleanField(default=False),
        ),
    ]
