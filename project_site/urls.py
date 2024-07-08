from django.urls import path, include

from .views import (project_site_list_view, project_site_detail_view, project_site_creation_form,
                    customer_project_suggestions, project_site_edit_form)

app_name = 'project_site'

urlpatterns = [
    path('', project_site_list_view, name='project_site_list_view'),
    path('customer_project_suggestions/', customer_project_suggestions, name='customer_project_suggestions'),
    path('project_site_creation_form/', project_site_creation_form, name='project_site_creation_form'),
    path('project_site_edit_form/<uuid:pk>/', project_site_edit_form, name='project_site_edit_form'),
    path('project_site_detail_view/<uuid:pk>/', project_site_detail_view, name='project_site_detail_view'),
]