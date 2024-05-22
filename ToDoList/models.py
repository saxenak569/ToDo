from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    date = models.DateField(null=True, default=datetime.now)
    to_do = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"