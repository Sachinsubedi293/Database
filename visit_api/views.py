from visit.models import visit
from .serializers import visitSerializer
from rest_framework import generics

class visitView(generics.ListCreateAPIView):
    queryset =visit.objects.all()
    serializer_class =visitSerializer

class visitDetails(generics.RetrieveDestroyAPIView):
    queryset =visit.objects.all()
    serializer_class =visitSerializer
