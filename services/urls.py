from django.urls import path
from .views import (services_list_view, fte_service_creation_form, customer_project_suggestions, project_site_suggestions, 
                    sales_order_suggestions, vendor_account_suggestions, vendor_project_suggestions, fte_service_detail_view)

app_name = 'services'

urlpatterns = [
    path('', services_list_view, name='services_list_view'),
    path('fte_service_creation_form/', fte_service_creation_form, name='fte_service_creation_form'),
    path('fte_service_detail_view/<uuid:pk>/', fte_service_detail_view, name='fte_service_detail_view'),
    path('customer_project_suggestions/', customer_project_suggestions, name='customer_project_suggestions'),
    path('project_site_suggestions/', project_site_suggestions, name='project_site_suggestions'),
    path('sales_order_suggestions/', sales_order_suggestions, name='sales_order_suggestions'),
    path('vendor_account_suggestions/', vendor_account_suggestions, name='vendor_account_suggestions'),
    path('vendor_project_suggestions/', vendor_project_suggestions, name='vendor_project_suggestions'),
]
