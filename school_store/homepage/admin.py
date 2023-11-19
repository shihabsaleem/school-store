from django.contrib import admin
from .models import Department, InfoDet, Course, Material


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Department, DepartmentAdmin)


class InfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'phone', 'email', 'department', 'course']


admin.site.register(InfoDet, InfoAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', ]

admin.site.register(Material)

admin.site.register(Course, CourseAdmin)
