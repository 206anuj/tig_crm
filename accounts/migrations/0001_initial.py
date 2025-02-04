# Generated by Django 4.2 on 2024-06-12 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ca_name', models.CharField(max_length=255)),
                ('ca_record_type', models.CharField(max_length=255)),
                ('ca_phone_number', models.CharField(blank=True, max_length=11)),
                ('ca_account', models.CharField(blank=True, max_length=255)),
                ('ca_account_owner', models.CharField(blank=True, max_length=255)),
                ('ca_type', models.CharField(choices=[('Prospect', 'Prospect'), ('Customer Direct', 'Customer Direct'), ('Customer Channel', 'Customer Channel'), ('Channel', 'Channel'), ('Partner / Reseller', 'Partner / Reseller'), ('Installation Partner', 'Installation Partner'), ('Technology Partner', 'Technology Partner'), ('Other', 'Other')], max_length=64)),
                ('ca_customer_code', models.CharField(blank=True, max_length=255)),
                ('ca_industray', models.CharField(blank=True, choices=[('IT', 'IT'), ('Agriculture', 'Agriculture'), ('Apparel', 'Apparel'), ('Banking', 'Banking'), ('Chemicals', 'Chemicals'), ('Construction', 'Construction'), ('Consulting', 'Consulting'), ('Education', 'Education'), ('Electronics', 'Electronics'), ('Energy', 'Energy'), ('Engineering', 'Engineering'), ('Finance', 'Finance'), ('Government', 'Government'), ('Healthcare', 'Healthcare'), ('Insurance', 'Insurance'), ('Machinery', 'Machinery'), ('Media', 'Media'), ('Recreation', 'Recreation'), ('Retail', 'Retail'), ('Shipping', 'Shipping'), ('Technology', 'Technology'), ('Biotechnology', 'Biotechnology'), ('Communications', 'Communications'), ('Entertainment', 'Entertainment'), ('Environmental', 'Environmental'), ('Food & Beverage', 'Food & Beverage'), ('Manufacturing', 'Manufacturing'), ('Not For Profit', 'Not For Profit'), ('Telecommunications', 'Telecommunications'), ('Transportation', 'Transportation'), ('Utilities', 'Utilities'), ('Other', 'Other')], max_length=64)),
                ('ca_description', models.TextField(blank=True, max_length=1024)),
                ('ca_payment_terms', models.CharField(blank=True, choices=[('NET0', 'NET0'), ('NET10', 'NET10'), ('NET30', 'NET30'), ('NET45', 'NET45'), ('NET60', 'NET60'), ('NET90', 'NET90')], max_length=64)),
                ('ca_billing_address', models.CharField(blank=True, max_length=1024)),
                ('ca_billing_street', models.TextField(blank=True, max_length=1024)),
                ('ca_billing_city', models.CharField(blank=True, max_length=255)),
                ('ca_billing_pin_code', models.CharField(blank=True, max_length=64)),
                ('ca_shipping_address', models.CharField(blank=True, max_length=1024)),
                ('ca_shipping_street', models.TextField(blank=True, max_length=1024)),
                ('ca_shipping_city', models.CharField(blank=True, max_length=255)),
                ('ca_shipping_pin_code', models.CharField(blank=True, max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ca_billing_country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_customer_accounts', to='cities_light.country')),
                ('ca_billing_state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_customer_accounts', to='cities_light.region')),
                ('ca_shipping_country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_customer_accounts', to='cities_light.country')),
                ('ca_shipping_state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_customer_accounts', to='cities_light.region')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
