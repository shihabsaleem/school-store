from .models import Department

def menu_links(request):
    links = Department.objects.all()

    return {'links': links}
