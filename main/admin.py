from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display=('first_name','mobile_no',)
    search_fields=('first_name','mobile_no')
admin.site.register(Patient,PatientAdmin)