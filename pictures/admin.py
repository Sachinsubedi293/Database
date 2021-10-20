from django.contrib import admin
from .models import pictures
# admin.site.register(Category

class picturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_filter = ("id",)
    search_fields = ['title', 'id']
    
  
admin.site.register(pictures, picturesAdmin)




