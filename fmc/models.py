from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Appliances(models.Model):
    appliance = models.CharField(max_length=64, null=64)
    part_name = models.CharField(max_length=64, null=True)
    model_number = models.CharField(max_length=64, null=True)
    part_number = models.CharField(max_length=64, null=True)
    url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.model_number + ' | Apt. ' + self.part_number

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

class Work(models.Model):
    
    company = models.CharField('Management Company', max_length=64, blank=True)
    address = models.CharField(max_length=64)
    apartment = models.CharField(max_length=64)
    city = models.CharField(max_length=64, null=True)
    zip_code = models.IntegerField('Zip Code', null=True)
    state = models.CharField(max_length=12, choices=STATE_CHOICES, default='NEW YORK')
    appliance = models.CharField(max_length=64)
    phone = models.CharField('Phone Number', max_length=12, null=True)
    comments = models.TextField(max_length=128, null=True, blank=True)
    private = models.CharField(max_length=12, choices=PRIVATE_CHOICES, default='')
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Pending')
    part = models.ManyToManyField(Appliances, related_name='add_part', blank=True)
    

    def __str__(self):
        return self.address + ' | Apt. ' + self.apartment

    def get_absolute_url(self):
        return reverse('create-work-order')