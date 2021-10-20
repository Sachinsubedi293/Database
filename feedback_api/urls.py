from django.urls import path
from .views import  PostView,feedbackDetails
from . import views

app_name = 'feedback_api'

urlpatterns = [
  path('feedback/', PostView.as_view(), name='feedback'),
  path('feedback/<int:pk>',feedbackDetails.as_view(),name='feedbackDetails'),
]