from django.db import models
from django.utils import timezone
# Create your models here.


class MyTime(models.Model):
    name = models.CharField(max_length=100)
    alarm = models.DateTimeField(default=timezone.now)
