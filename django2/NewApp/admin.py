from django.contrib import admin

from .models import Data, Department, Student

# Register your models here.
admin.site.register(Data)
admin.site.register(Student)
admin.site.register(Department)