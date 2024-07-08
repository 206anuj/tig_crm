from django.contrib import admin
from .models import CustomerAccount, VendorAccount

# Register your models here.

admin.site.register(CustomerAccount)
admin.site.register(VendorAccount)