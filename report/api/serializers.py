from rest_framework import serializers
from report.models import *
from accounts.models import *


class ReportSerializer(serializers.ModelSerializer):

	class Meta:
		model = Report
		fields = ['id', 'doctor', 'patient', 'disease']

	

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