"""
Base url = 127.0.0.1:8000/


127.0.0.1:8000/accounts/login

127.0.0.1:8000/accounts/logout

127.0.0.1:8000/accounts/register

127.0.0.1:8000/accounts/edit_profile
"""

from django.urls import path
from .views import login_view, logout_view, register_view


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    # path('edit_profile'),
]