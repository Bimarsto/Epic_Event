from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Client(models.Model):
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)
    email = models.EmailField(max_length=100,
                              null=False)
    phone = models.CharField(max_length=20, null=False)
    mobile = models.CharField(max_length=20, null=False)
    company_name = models.CharField(max_length=250, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.PROTECT)


class Contract(models.Model):
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.PROTECT)
    client = models.ForeignKey(to='Client',
                               on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payement_due = models.DateTimeField()


class Event(models.Model):
    EVENT_STATUS = [
        ('Upcoming', 'upcoming'),
        ('In progress', 'in_progress'),
        ('Completed', 'completed')
    ]

    client = models.ForeignKey(to='Client',
                               on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                        on_delete=models.PROTECT)
    event_status = models.CharField(max_length=25,
                                    choices=EVENT_STATUS,
                                    default='Upcoming')
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    note = models.TextField(max_length=1000)
