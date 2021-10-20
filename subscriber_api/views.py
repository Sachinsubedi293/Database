
# Create your views here.
from subscriber.models import subscriber
from .serializers import PostSerializer
from rest_framework import generics

class PostView(generics.ListCreateAPIView):
    queryset = subscriber.objects.all()
    serializer_class = PostSerializer

class subscriberDetails(generics.RetrieveDestroyAPIView):
    queryset = subscriber.objects.all()
    serializer_class = PostSerializer