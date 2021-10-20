from django.urls import path
from .views import picturesView,picturesDetails

app_name = 'pictures_api'

urlpatterns = [
    path('pictures/', picturesView.as_view(), name='pictures'),
    path('pictures/<int:pk>/',picturesDetails.as_view(),name='picturesdetail')
]