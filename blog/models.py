from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class blogs(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='blogs/%Y/%m/%d', blank=True,null=True)
    content1 = models.TextField(blank=True,null=True)
    image1 = models.ImageField(upload_to='blogs/%Y/%m/%d', blank=True,null=True)
    content2 = models.TextField(blank=True,null=True)
    image2 = models.ImageField(upload_to='blogs/%Y/%m/%d', blank=True,null=True)
    content3 = models.TextField(blank=True,null=True)
    image3 = models.ImageField(upload_to='blogs/%Y/%m/%d', blank=True,null=True)
    content4 = models.TextField(blank=True,null=True)
    author = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title