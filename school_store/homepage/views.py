from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Department, Course, InfoDet, Material


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
    departments = Department.objects.all()
    # Fetch all materials for the form
    materials = Material.objects.all()

    return render(request, 'form.html', {'departments': departments, 'materials': materials})

def add_info(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        purpose = request.POST.get('purpose')
        department_id = request.POST.get('department')
        course_id = request.POST.get('course')
        materials = request.POST.getlist('materials')

        # Retrieve Department and Course instances
        department = get_object_or_404(Department, id=department_id)
        course = get_object_or_404(Course, id=course_id)

        # Create InfoDet instance and save
        infodata = InfoDet(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            purpose=purpose,
            department=department,
            course=course
        )
        infodata.save()

        # Retrieve Material objects associated with selected materials
        materials_objs = Material.objects.filter(name__in=materials)
        infodata.material.add(*materials_objs)

    return render(request, 'success.html')