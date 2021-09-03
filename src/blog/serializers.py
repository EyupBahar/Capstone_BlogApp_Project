from rest_framework import serializers
from .models import Post
from django.utils.timezone import now

class PostSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id","title","user","content","image","publish_date","last_updated","category","status"]
    
    # def get_days_since_joined(self, obj):
    #     return (now() - obj.date_joined).days