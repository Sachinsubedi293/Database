from rest_framework import serializers
from feedback.models import feedback
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = feedback
        fields = "__all__"