from django.contrib import admin
from .models import Department, Course

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Department, DepartmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'seats']
    list_editable = ['seats']
    list_per_page = 20

admin.site.register(Course, CourseAdmin)
