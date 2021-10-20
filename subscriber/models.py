from django.db import models
from django.contrib.auth.models import User

class subscriber(models.Model):
    email = models.CharField(max_length=9999999, unique=True)
    user = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
