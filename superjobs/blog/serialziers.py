from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """TODO: def Post serializer
    return: TODO
    """
    class Meta:
        model = Post
        fields = ('id', 'title', 'description',
                  'created_at', 'tag', 'views', 'slug')
