from rest_framework import serializers
from subscriber.models import subscriber
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = subscriber
        fields = "__all__"