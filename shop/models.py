from django.db import models

# Create your models here

class category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    

    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='media/products/%Y/%m/', blank=True,null=True)
    extraimage1 = models.ImageField(upload_to='media/products/%Y/%m', blank=True, null=True)
    extraimage2 = models.ImageField(upload_to='media/products/%Y/%m', blank=True, null=True)
    extraimage3 = models.ImageField(upload_to='media/products/%Y/%m', blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    sale = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        index_together = (('id' ),)
    def __str__(self):
        return self.name
        