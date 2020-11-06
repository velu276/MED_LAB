from django.urls import path
from .views import (
		report_detail_view,
		report_list_view,
		report_detail_data_view,
		report_update_view,
		report_delete_view,
		report_create_view,
		test_result_delete_view,
		test_result_create_view,
		lab_test_create_view,
	)

app_name = 'report'

urlpatterns = [
	path('', report_list_view, name='report-list'),
	path('detail/', report_detail_view, name='report-detail'),
	path('detail/data/', report_detail_data_view, name='report-detail-data'),
	
	path('update', report_update_view, name='report-update'),

	path('delete/report', report_delete_view, name='report-delete'),
	path('delete/test_result', test_result_delete_view, name='test_result-delete'),

	path('create/report', report_create_view, name='report-create'),
	path('create/test_result', test_result_create_view, name='test_result-create'),
	path('create/lab_test', lab_test_create_view, name='lab_test-create'),
]
