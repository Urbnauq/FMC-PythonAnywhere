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

class Work(models.Model):

    company = models.CharField('Management Company', max_length=64, blank=True)
    address = models.CharField(max_length=64)
    apartment = models.CharField(max_length=64)
    city = models.CharField(max_length=64, null=True)
    zip_code = models.IntegerField('Zip Code', null=True)
    state = models.CharField(max_length=12, choices=STATE_CHOICES, default='NEW YORK')
    appliance = models.CharField(max_length=64)
    phone = models.CharField('Phone Number', max_length=64, null=True)
    comments = models.TextField(max_length=128, null=True, blank=True)
    private = models.CharField(max_length=12, choices=PRIVATE_CHOICES, default='')
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Pending')
    date_added = models.DateTimeField(auto_now_add=True, null=True)
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