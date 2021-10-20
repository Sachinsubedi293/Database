from django.urls import path
from .views import  PostView,subscriberDetails
from . import views

app_name = 'subscriber_api'

urlpatterns = [
  path('subscriber/', PostView.as_view(), name='subscriber'),
  path('subscriber/<int:pk>',subscriberDetails.as_view(),name='subscriberDetails'),
]