
# Create your views here.
from feedback.models import feedback
from .serializers import PostSerializer
from rest_framework import generics

class PostView(generics.ListCreateAPIView):
    queryset = feedback.objects.all()
    serializer_class = PostSerializer

class feedbackDetails(generics.RetrieveDestroyAPIView):
    queryset = feedback.objects.all()
    serializer_class = PostSerializer