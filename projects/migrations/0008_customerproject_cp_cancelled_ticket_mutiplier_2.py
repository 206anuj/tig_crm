# Generated by Django 4.2 on 2024-06-20 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_customerproject_cp_last_billing_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerproject',
            name='cp_cancelled_ticket_mutiplier_2',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
