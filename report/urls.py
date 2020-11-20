from django.urls import path
from django.views.generic import TemplateView

app_name = 'report'

urlpatterns = [
	path('', TemplateView.as_view(template_name='report/home.html'), name='report-home')

]
