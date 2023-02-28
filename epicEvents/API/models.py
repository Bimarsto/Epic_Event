from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(AbstractUser):
#     TEAM = [
#         ('not_assigned', 'not_assigned'),
#         ('sales', 'sales'),
#         ('support', 'support'),
#     ]
#     team = models.CharField(choices=TEAM, max_length=20, default='not_assigned')


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
    payment_due = models.DateTimeField()


class Event(models.Model):
    client = models.ForeignKey(to='Client',
                               on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                        on_delete=models.PROTECT)
    event_status = models.ForeignKey(to='EventStatus',
                                     on_delete=models.PROTECT)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    note = models.TextField(max_length=1000)


class EventStatus(models.Model):
    status = models.CharField(max_length=20)
