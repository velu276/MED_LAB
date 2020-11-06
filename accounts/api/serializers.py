from rest_framework import serializers
from report.models import *
from accounts.models import *


class UserRegistrationSerializer(serializers.ModelSerializer):
	
	password2 = serializers.CharField(style={'input_type':'password'}, write_only = True)

	class Meta:
		model = MyUser
		fields = ['phone', 'name', 'age', 'gender', 'password', 'password2']
		extra_kwargs = {
			'password':{'write_only':True}
		}

	def validate(self, data):
		if 'age' not in data:
			data['age'] = MyUser._meta.get_field('age').get_default()
		if 'gender' not in data:
			data['gender'] = MyUser._meta.get_field('gender').get_default()
		return data

	def save(self):
		user = MyUser(
				phone = self.validated_data['phone'],
				name = self.validated_data['name'],
				age = self.validated_data['age'],
				gender = self.validated_data['gender'],
			)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']

		if password != password2:
			raise serializers.ValidationError({'password':'Passwords must match'})

		user.set_password(password)
		user.save()
		return user