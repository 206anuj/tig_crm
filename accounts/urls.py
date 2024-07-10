
from django.urls import path

from .views import (customer_accounts_list_view, customer_account_creation_form, customer_account_detail_view, 
                    get_states_by_country, select_account_type, customer_account_edit_form, upload_file_view,
                    vendor_account_detail_view, vendor_account_creation_form, vendor_account_edit_form)

app_name = 'accounts'

urlpatterns = [
     path('', customer_accounts_list_view, name='customer_accounts_list_view'),
     path('select_account_type/', select_account_type, name='select_account_type'),
     path('get_states_by_country/', get_states_by_country, name='get_states_by_country'),
     path('customer_account_creation_form/', customer_account_creation_form, name='customer_account_creation_form'),
     path('vendor_account_creation_form/', vendor_account_creation_form, name='vendor_account_creation_form'),
     path('customer_account_detail_view/<uuid:pk>/', customer_account_detail_view, name='customer_account_detail_view'),
     path('vendor_account_detail_view/<uuid:pk>/', vendor_account_detail_view, name='vendor_account_detail_view'),
     path('customer_account_edit_form/<uuid:pk>/', customer_account_edit_form, name='customer_account_edit_form'),
     path('vendor_account_edit_form/<uuid:pk>/', vendor_account_edit_form, name='vendor_account_edit_form'),
     path('upload_file_view/', upload_file_view, name='upload_file_view'),
    ]