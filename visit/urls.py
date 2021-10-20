from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import path

app_name = 'visit'
urlpatterns = [
    path('visit/',views.visit, name='visit'),  
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)