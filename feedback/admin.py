from django.contrib import admin
from .models import feedback

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','content','created_on')
    list_filter = ("content",)
    search_fields = ['id', 'content']

  
admin.site.register(feedback, PostAdmin)