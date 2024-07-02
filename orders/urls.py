from django.urls import path

from .views import (sales_order_list_view, sales_order_detail_view, 
                    sales_order_creation_form, customer_account_suggestions,
                    customer_project_suggestions, sales_order_edit_form)
                    


app_name = 'orders'

urlpatterns = [
    path('', sales_order_list_view, name='sales_order_list_view'),
    # path('select_account_type/', select_account_type, name='select_account_type'),
    path('sales_order_creation_form/', sales_order_creation_form, name='sales_order_creation_form'),
    path('customer_account_suggestions/', customer_account_suggestions, name='customer_account_suggestions'),
    path('customer_project_suggestions/', customer_project_suggestions, name='customer_project_suggestions'),
    path('sales_order_detail_view/<uuid:pk>/', sales_order_detail_view, name='sales_order_detail_view'),
    path('sales_order_edit_form/<uuid:pk>/', sales_order_edit_form, name='sales_order_edit_form'),
]