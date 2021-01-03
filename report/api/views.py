from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from report.models import *
from accounts.models import *
from .serializers import (
		ReportSerializer,
		TestResultSerializer,
		ReportCreateSerializer,
		TestResultCreateSerializer,
		LabTestSerializer
	)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def report_list_view(request):
	try:
		user = request.user
		if user.is_lab_staff:
			reports = Report.objects.filter(doctor=request.user.id)
		else:
			reports = Report.objects.filter(patient=request.user.id)
			
	except Report.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	serializer = ReportSerializer(reports, many=True)
	return Response(serializer.data)



@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def report_detail_view(request):
	try:
		report = Report.objects.get(id=request.GET['id'])
	except Report.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	user = request.user
	if report.patient != user and user.is_lab_staff == False:
		return Response({'respose':"You don't have permission to view this report."})

	serializer = ReportSerializer(report)
	return Response(serializer.data)



@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def report_detail_data_view(request):
	try:
		report = Report.objects.get(id=request.GET['id'])
	except Report.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	user = request.user
	if report.patient != user and user.is_lab_staff == False:
		return Response({'respose':"You don't have permission to view this report."})

	tests = Test_result.objects.filter(report=report)
	serializer = TestResultSerializer(tests, many=True)
	return Response(serializer.data)


@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def report_update_view(request):
	try:
		report = Report.objects.get(id=request.GET['id'])
	except Report.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	user = request.user
	if user.is_lab_staff == False:
		return Response({'respose':"You don't have permission to edit this report."})

	serializer = ReportSerializer(report, data=request.data)

	data = {}
	
	if serializer.is_valid():
		serializer.save()
		data['success'] = 'update successful'
		return Response(data=data)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def report_delete_view(request):
	try:
		report = Report.objects.get(id=request.GET['id'])
	except Report.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	user = request.user
	if user.is_lab_staff == False:
		return Response({'respose':"You don't have permission to delete this report."})

	operation = report.delete()
	data = {}
	if operation:
		data['success'] = 'delete successful'
	else:
		data['failure'] = 'delete failed'
	return Response(data=data)

@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def test_result_delete_view(request):
	try:
		result = Test_result.objects.get(id=request.GET['id'])
	except Test_result.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	user = request.user
	if user.is_lab_staff == False:
		return Response({'respose':"You don't have permission to delete Test Results."})

	operation = result.delete()
	data = {}
	if operation:
		data['success'] = 'delete successful'
	else:
		data['failure'] = 'delete failed'
	return Response(data=data)


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def report_create_view(request):

	user = request.user
	if user.is_lab_staff == False:
		return Response({'respose':"You don't have permission to create a report."})

	report = Report(doctor=user)

	serializer = ReportCreateSerializer(report, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def test_result_create_view(request):

	user = request.user
	if user.is_lab_staff == False:
		return Response({'respose':"You don't have permission to create Test Results."})


	serializer = TestResultCreateSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def lab_test_create_view(request):

	user = request.user
	if user.is_superuser == False:
		return Response({'respose':"You don't have permission to add a new Test."})


	serializer = LabTestSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)