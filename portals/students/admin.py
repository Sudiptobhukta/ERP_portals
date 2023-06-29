from django.contrib import admin
from students.models import student,File,attendence,report

# Register your models here.
admin.site.register(student)
admin.site.register(File)
admin.site.register(attendence)
admin.site.register(report)

