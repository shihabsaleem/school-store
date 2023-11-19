from .models import Department, Course, Material


def menu_links(request):
    links = Department.objects.all()
    return {'links': links}


def dept_links(request):
    dept_link = Department.objects.all()
    return {'dept_link': dept_link}


def course_links(request):
    course_link = Course.objects.all()
    return {'course_link': course_link}


def material_links(request):
    material_link = Material.objects.all()
    return {'material_link': material_link}
