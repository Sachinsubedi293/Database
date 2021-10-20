from django.db import models

# Create your models here


class pictures(models.Model):
    name = models.CharField(max_length=400, db_index=True)
    image = models.ImageField(upload_to='pictures/%Y/%m/', blank=True,null=True)
    by = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        index_together = (('id' ),)
    def __str__(self):
        return self.name
        