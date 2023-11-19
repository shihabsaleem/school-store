from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Department


def dept(request, dept_slug=None):
    department = Department.objects.all()

    if dept_slug:
        dept_page = get_object_or_404(Department, slug=dept_slug)
    else:
        dept_page = None

    return render(request, 'dept.html', {'dept_page': dept_page, 'department': department})


def home(request):
    return render(request, "index.html")


def form(request):
    return render(request, 'form.html')
