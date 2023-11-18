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
