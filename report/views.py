from django.shortcuts import render
from .models import *

# Create your views here.

def detail(request):
	tests = Test_result.objects.filter(report=2)
	context = {'tests':tests, 'report':Report.objects.get(id=1)}
	return render(request, 'report/detail.html', context)