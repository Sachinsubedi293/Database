from django.contrib import admin
from .models import subscriber

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','email','created_on')
    list_filter = ("email",)
    search_fields = ['id', 'email']

  
admin.site.register(subscriber, PostAdmin)