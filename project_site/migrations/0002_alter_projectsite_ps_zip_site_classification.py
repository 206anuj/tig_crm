# Generated by Django 4.2 on 2024-07-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsite',
            name='ps_ZIP_site_classification',
            field=models.CharField(blank=True, choices=[('Metro', 'Metro'), ('Rural', 'Rural'), ('Regional', 'Regional')], max_length=64),
        ),
    ]
