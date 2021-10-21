from django.contrib import admin
from .models import blogs


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['id', 'title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(blogs, PostAdmin)
