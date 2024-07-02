from django.urls import path, include

from .views import (project_site_list_view, project_site_detail_view, project_site_creation_form)

app_name = 'project_site'

urlpatterns = [
    path('', project_site_list_view, name='project_site_list_view'),
    path('project_site_creation_form/', project_site_creation_form, name='project_site_creation_form'),
    path('project_site_detail_view/<uuid:pk>/', project_site_detail_view, name='project_site_detail_view'),
]