# Generated by Django 4.2 on 2024-06-26 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_salesorder_so_po_amount_utilised'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='so_po_amount',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='so_po_amount_utilised',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='so_po_balance',
            field=models.CharField(max_length=10),
        ),
    ]
