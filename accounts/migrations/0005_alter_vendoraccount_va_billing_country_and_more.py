# Generated by Django 4.2 on 2024-07-05 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('accounts', '0004_vendoraccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendoraccount',
            name='va_billing_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='va_billing_country', to='cities_light.country'),
        ),
        migrations.AlterField(
            model_name='vendoraccount',
            name='va_billing_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='va_billing_state', to='cities_light.region'),
        ),
        migrations.AlterField(
            model_name='vendoraccount',
            name='va_shipping_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='va_shipping_country', to='cities_light.country'),
        ),
        migrations.AlterField(
            model_name='vendoraccount',
            name='va_shipping_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='va_shipping_state', to='cities_light.region'),
        ),
    ]
