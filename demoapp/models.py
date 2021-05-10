from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Company(models.Model):
    """
    Model for Company information
    """
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('demoapp:company_detail', kwargs={'pk': self.pk})

class Employee(models.Model):
    """
    Model for Employee information
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=32, blank=True)
    state = models.CharField(max_length=32, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)

    def get_absolute_url(self):
        return reverse('demoapp:employee_detail', kwargs={'pk': self.pk})
