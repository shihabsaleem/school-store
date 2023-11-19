from django.db import models
from django.urls import reverse

class Department(models.Model):
    name = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='dept', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def get_url(self):
        return reverse('homepage:dept', args=[self.slug])

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=150, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class InfoDet(models.Model):
    name = models.CharField(max_length=150)
    dob = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Prefer Not to Say'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    PURPOSE_CHOICES = [
        ('Enquiry', 'Enquiry'),
        ('Place Order', 'Place Order'),
        ('Return', 'Return'),
    ]
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES)
    material = models.ManyToManyField(Material)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
