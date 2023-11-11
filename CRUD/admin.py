from django.contrib import admin

# Register your models here.

from .models import *

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone')

admin.site.register(Employees, EmployeesAdmin)