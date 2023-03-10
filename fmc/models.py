from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

STATE_CHOICES = (
    ('New York', 'New York'),
    ('New York', 'New Jersey'),
)

PRIVATE_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('2C2R', '2C2R'),
    ('Completed', 'Completed'),
)

TECHNICIAN = (
    ('', '-------'),
    ('Canela', 'Canela'),
    ('Eddie', 'Eddie'),
    ('Jansel', 'Jansel'),
    ('Jose', 'Jose'),
    ('Luis', 'Luis'),
    ('Oscar A.', 'Oscar A.'),
    ('Oscar', 'Oscar'),
)

class Work(models.Model):

    company = models.CharField('Management Company', max_length=64, blank=True)
    address = models.CharField(max_length=64)
    apartment = models.CharField(max_length=64)
    city = models.CharField(max_length=64, null=True)
    zip_code = models.IntegerField('Zip Code', null=True, blank=True)
    state = models.CharField(max_length=12, choices=STATE_CHOICES, default='NEW YORK')
    appliance = models.CharField(max_length=64)
    phone = models.CharField('Phone Number', max_length=64, null=True, blank=True)
    comments = models.CharField('Description', max_length=64, null=True, blank=True)
    private = models.CharField(max_length=12, choices=PRIVATE_CHOICES, default='')
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Pending')
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    logo = models.ImageField(null=True, blank=True)
    requested = models.DateField(null=True, blank=True)
    completed = models.DateField('Date Complete', null=True, blank=True)
    complete_by = models.CharField('Complete By', max_length=12, choices=TECHNICIAN, blank=True, default='')
    #part = models.ManyToManyField(Appliances, related_name='add_part', blank=True)

    def __str__(self):
        return self.address + ' | Apt. ' + self.apartment

    def get_absolute_url(self):
        return reverse('create-work-order')

class Appliances(models.Model):
    part_address = models.ForeignKey(Work, related_name='address_appliances', on_delete=models.CASCADE)
    appliance = models.CharField(max_length=64, null=True)
    part_name = models.CharField(max_length=64, null=True)
    model_number = models.CharField(max_length=64, null=True)
    part_number = models.CharField(max_length=64, null=True)
    url = models.URLField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.model_number + ' | Apt. ' + self.part_number