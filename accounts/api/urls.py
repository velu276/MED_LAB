from django.urls import path
from .views import (
		user_registration
	)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'accounts'

urlpatterns = [
	path('register', user_registration, name='user-register'),
	path('login', obtain_auth_token, name='user-register'),
]
