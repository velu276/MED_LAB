from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
	search_fields = ('name', 'phone')
	ordering = ('name',)
	list_display = ('name', 'phone', 'is_active', 'is_lab_staff', 'is_superuser')

	fieldsets = (
		('About', {'fields': ('name', 'phone')}),
		('Permissions', {'fields': ('is_lab_staff', 'is_active', 'is_superuser')}),
		('Personal', {'fields':('age', 'gender')})
	)

	add_fieldsets = (
		(None, {
				'classes': ('wide',),
				'fields':('name', 'phone', 'password1', 'password2', 'gender', 'age', 'is_active', 'is_lab_staff', 'is_superuser')
			}
		),
	)

admin.site.register(MyUser, UserAdminConfig)