from django.urls import path
from .views import visitView,visitDetails

app_name = 'visit_api'

urlpatterns = [
    path('visit/', visitView.as_view(), name='visit'),
    path('visit/<int:pk>/',visitDetails.as_view(),name='visitsdetail')
]