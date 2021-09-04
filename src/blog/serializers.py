from rest_framework import serializers
from .models import Post
from django.utils.timezone import now

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__',
        # fields = ["id","title","user","content","image","publish_date","last_updated","category","status"]
