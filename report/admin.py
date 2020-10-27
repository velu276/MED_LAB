from django.contrib import admin
from .models import *

@admin.register(Lab_test)
class LabTestAdminConfig(admin.ModelAdmin):
	search_fields = ('name',)
	ordering = ('name',)
	list_display = ('name', 'start_value', 'end_value', 'units', 'cost')

	fieldsets = (
		(None, {'fields': ('name', 'start_value', 'end_value', 'units', 'cost')}),
	)

	add_fieldsets = (
		(None, {
				'classes': ('wide',),
				'fields':('name', 'start_value', 'end_value', 'units', 'cost')
				}
		),
	)
	
@admin.register(Disease)
class DiseaseAdminConfig(admin.ModelAdmin):
	search_fields = ('name',)
	ordering = ('name',)
	list_display = ('name',)

	fieldsets = (
		(None, {'fields': ('name', 'tests')}),
	)

	add_fieldsets = (
		(None, {
				'classes': ('wide',),
				'fields':('name', 'tests')
				}
		),
	)


@admin.register(Report)
class ReportAdminConfig(admin.ModelAdmin):
	search_fields = ('patient',)
	ordering = ('-date_issued',)
	list_display = ('patient', 'doctor', 'date_issued', 'disease')

	fieldsets = (
		(None, {'fields': ('patient', 'doctor', 'disease')}),
	)

	add_fieldsets = (
		(None, {
				'classes': ('wide',),
				'fields':('patient', 'doctor', 'date_issued', 'disease')
				}
		),
	)


@admin.register(Test_result)
class TestResultAdminConfig(admin.ModelAdmin):
	search_fields = ('report',)
	ordering = ('report',)
	list_display = ('report', 'lab_test', 'result')

	fieldsets = (
		(None, {'fields': ('report', 'lab_test', 'result',)}),
	)

	add_fieldsets = (
		(None, {
				'classes': ('wide',),
				'fields':('report', 'lab_test', 'result')
				}
		),
	)
