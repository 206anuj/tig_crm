from django.contrib import admin
from .models import CustomerProject, VendorProject

# Register your models here.

admin.site.register(CustomerProject)
admin.site.register(VendorProject)
