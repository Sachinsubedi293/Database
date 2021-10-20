from django.db import models
from django.contrib.auth.models import User

class feedback(models.Model):
    content = models.CharField(max_length=9999999, unique=False)
    author = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
