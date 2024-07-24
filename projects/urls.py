from django.urls import path
 
from .views import (customer_project_list_view, customer_project_creation_form, select_project_type,
                    customer_account_suggestions, customer_project_detail_view, customer_project_edit_form,
                    vendor_project_creation_form,vendor_account_suggestions,customer_project_suggestions, vendor_project_detail_view,vendor_project_edit_form)
                   
 
 
app_name = 'projects'
 
urlpatterns = [
    path('', customer_project_list_view, name='customer_project_list_view'),
    path('select_project_type/', select_project_type, name='select_project_type'),
    path('customer_project_creation_form/', customer_project_creation_form, name='customer_project_creation_form'),
    path('customer_account_suggestions/', customer_account_suggestions, name='customer_account_suggestions'),
    path('customer_project_detail_view/<uuid:pk>/', customer_project_detail_view, name='customer_project_detail_view'),
    path('customer_project_edit_form/<uuid:pk>/', customer_project_edit_form, name='customer_project_edit_form'),
    path('vendor_project_creation_form/', vendor_project_creation_form, name="vendor_project_creation_form" ),
    path('vendor_account_suggestions/', vendor_account_suggestions, name='vendor_account_suggestions'),
    path('customer_project_suggestions/', customer_project_suggestions, name='customer_project_suggestions'),
    path('vendor_project_detail_view/<uuid:pk>/', vendor_project_detail_view, name='vendor_project_detail_view'),
    path('vendor_project_edit_form/<uuid:pk>/', vendor_project_edit_form, name='vendor_project_edit_form')
]