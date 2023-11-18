from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Department, Course

def dept(request, dept_slug=None):
    dept_page = None
    department = Department.objects.all()

    if dept_slug is not None:
        dept_page = get_object_or_404(Department, slug=dept_slug)
        course_list = Course.objects.filter(dept=dept_page)
    else:
        course_list = Course.objects.all()

    return render(request, 'dept.html', {'dept_page': dept_page, 'department': department, 'course_list': course_list})

def home(request):
    return render(request, "index.html")


def course(request, dept_slug, course_slug):
    department = get_object_or_404(Department, slug=dept_slug)
    try:
        course = get_object_or_404(Course, dept=department, name=course_slug)
    except Course.DoesNotExist:
        raise Http404("Course does not exist")

    return render(request, 'course.html', {'course': course, 'department': department})