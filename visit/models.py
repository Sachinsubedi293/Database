from django.db import models

# Create your models here


class visit(models.Model):
    name = models.CharField(max_length=400, db_index=True)
    image = models.ImageField(upload_to='visit/%Y/%m/', blank=True,null=True)
    image1 = models.ImageField(upload_to='visit/1/%Y/%m/', blank=True,null=True)
    image2 = models.ImageField(upload_to='visit/1/2/%Y/%m/', blank=True,null=True)
    description = models.TextField(blank=True)
    map_image = models.ImageField(upload_to='visit/map/%Y/%m/', blank=True,null=True)
    map_description = models.TextField(blank=True)
    city = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        index_together = (('id' ),)
    def __str__(self):
        return self.name
        