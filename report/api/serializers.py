from rest_framework import serializers
from report.models import *
from accounts.models import *


class ReportSerializer(serializers.ModelSerializer):

	doctor = serializers.SerializerMethodField('get_doctor_name')
	patient = serializers.SerializerMethodField('get_patient_name')
	disease = serializers.SerializerMethodField('get_disease_name')
	date_issued = serializers.SerializerMethodField('get_date')

	class Meta:
		model = Report
		fields = ['id', 'doctor', 'patient', 'disease', 'date_issued']

	
	def get_doctor_name(self, report):
		return report.doctor.name

	def get_patient_name(self, report):
		return report.patient.name

	def get_disease_name(self, report):
		return report.disease.name

	def get_date(self, report):
		return report.date_issued.strftime('%d %b %y')

	

class ReportCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Report
		fields = ['id', 'patient', 'disease']


class TestResultSerializer(serializers.ModelSerializer):

	units = serializers.SerializerMethodField('get_test_units')

	class Meta:
		model = Test_result
		fields = ['id', 'lab_test', 'result', 'units']


	def get_test_units(self, Test_result):
		return Test_result.lab_test.units


class TestResultCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Test_result
		fields = ['report', 'lab_test', 'result']


class LabTestSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lab_test
		fields = ['name', 'cost', 'start_value', 'end_value', 'units']