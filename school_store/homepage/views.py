from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Course

def dept(request, dept_slug=None):
    dept_page = None
    course_list = None
    department = Department.objects.all()

    if dept_slug is not None:
        dept_page = get_object_or_404(Department, slug=dept_slug)
        course_list = Course.objects.filter(category=dept_page, available=True)
    else:
        course_list = Course.objects.filter(available=True)

    return render(request, 'dept.html', {'dept_page': dept_page, 'department': department})

def home(request):
    return render(request, "index.html")


def course(request, dept_slug, course_slug):
    try:
        product = Course.objects.get(dept__slug=dept_slug, slug=course_slug)
    except Exception as e:
        raise e

    return render(request, 'dept.html', {'product': product})

