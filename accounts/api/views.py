from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from report.models import *
from accounts.models import *
from .serializers import (
		UserRegistrationSerializer
	)
from rest_framework.authtoken.models import Token


@api_view(['POST',])
def user_registration(request):

	serializer = UserRegistrationSerializer(data=request.data)
	data = {}
	if serializer.is_valid():
		user = serializer.save()
		data['response'] = 'success'
		data['phone'] = user.phone
		data['name'] = user.name
		token = Token.objects.get(user=user).key
		data['token'] = token
	else:
		data = serializer.errors
	return Response(data)