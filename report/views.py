from django.shortcuts import render
from .models import Report, Test_result, Disease, Lab_test

# Create your views here.

def detail(request):
	tests = Test_result.objects.filter(report= request.GET['id'])
	context = {'tests':tests, 'report':Report.objects.get(id=request.GET['id'])}
	return render(request, 'report/detail.html', context)