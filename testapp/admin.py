from django.contrib import admin
from testapp.models import EmployeeModel
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=["id","emp_id","emp_name","emp_sal","emp_addr"]
    search_fields=["emp_id"]
admin.site.register(EmployeeModel,EmployeeAdmin)