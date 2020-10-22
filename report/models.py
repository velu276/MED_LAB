from django.db import models
from accounts.models import MyUser
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Lab_test(models.Model):
	name = models.CharField(_('Test Name'), max_length=50, unique=True)
	cost = models.IntegerField(default = 10)
	start_value = models.CharField(max_length=15)
	end_value = models.CharField(max_length=15)
	units = models.CharField(max_length=15)

	def __str__(self):
		return self.name;


class Disease(models.Model):
	name = models.CharField(_('Disease Name'), max_length=100, unique=True)
	tests = models.ManyToManyField(Lab_test)

	def __str__(self):
		return self.name;



class Report(models.Model):
	date_issued = models.DateTimeField(auto_now_add=True)
	doctor = models.ForeignKey(MyUser, on_delete = models.SET('anonymous'), related_name='doctor')
	patient = models.ForeignKey(MyUser, on_delete = models.CASCADE, related_name='patient')
	disease = models.ForeignKey(Disease, on_delete = models.PROTECT)

	def __str__(self):
		return self.patient.name + "'s report for " + self.disease.name + " on " + (self.date_issued).strftime('%d-%m-%Y');


class Test_result(models.Model):
	report = models.ForeignKey(Report, on_delete = models.CASCADE)
	lab_test = models.ForeignKey(Lab_test, on_delete = models.SET('Test not avilable'))
	result = models.CharField(max_length=15)