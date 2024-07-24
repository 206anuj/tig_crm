from django.urls import path
from . views import (user_login, user_logout, home_page)

app_name = 'home'

urlpatterns = [
    path('', user_login, name='user_login'),
    path('user_logout/', user_logout, name='user_logout'),
    path('home/', home_page, name='home_page'),
  
]
