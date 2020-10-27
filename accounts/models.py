from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
 
# Create your models here.

class MyUserManager(BaseUserManager):

	def create_user(self, phone, name, password, **other_fields):

		if not phone:
			raise ValueError(_('You must provide your phone number'))
		if not name:
			raise ValueError(_('You must provide your name'))

		user = self.model(
				phone = phone,
				name = name,
				**other_fields
			)
		user.set_password(password)
		user.save()
		return user


	def create_superuser(self, phone, name, password, **other_fields):
		other_fields.setdefault('is_staff', True)
		other_fields.setdefault('is_superuser', True)
		other_fields.setdefault('is_admin', True)

		if other_fields.get('is_staff') is not True:
			raise ValueError(_('SuperUser must be given is_staff=True'))

		if other_fields.get('is_superuser') is not True:
			raise ValueError(_('SuperUser must be given is_superuser=True'))

		if other_fields.get('is_admin') is not True:
			raise ValueError(_('SuperUser must be given is_admin=True'))

		return self.create_user(phone, name, password, **other_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):

	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)

	phone = models.CharField(_('phone number'), max_length=10, unique=True)
	name = models.CharField(max_length=100, unique=False)
	age = models.IntegerField(default = 30)
	is_lab_staff = models.BooleanField(default=False)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'phone'
	REQUIRED_FIELDS = ['name']

	def __str__(self):
		return self.name+", "+self.phone