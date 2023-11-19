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
        return '{}'.format(self.name)


class Course(models.Model):
    name = models.CharField(max_length=150, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class InfoDet(models.Model):
    name = models.CharField(max_length=150)
    dob = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Prefer No to Say'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
