from django.contrib import admin
from .models import visit
# admin.site.register(Category

class visitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_filter = ("id",)
    search_fields = ['title', 'id']
    
  
admin.site.register(visit, visitAdmin)




