# Generated by Django 4.2 on 2024-07-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_alter_fteserivce_fte_serivce_vendor_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fteserivce',
            name='fte_serivce_customer_quote_po_conversion_rate',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
