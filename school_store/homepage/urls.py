from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='home'),
    path('dept/<slug:dept_slug>/', views.dept, name='dept'),
    path('form/', views.form, name='form'),
]
