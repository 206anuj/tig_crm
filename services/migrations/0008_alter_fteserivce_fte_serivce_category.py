# Generated by Django 4.2 on 2024-07-18 07:22

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_fteserivce_fte_serivce_subtype_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fteserivce',
            name='fte_serivce_category',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('EUC(End User Computing)', 'EUC(End User Computing)'), ('Network', 'Network'), ('Server', 'Server'), ('Storage', 'Storage')], max_length=1024),
        ),
    ]
