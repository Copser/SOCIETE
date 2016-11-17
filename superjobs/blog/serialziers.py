from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """TODO: def Post serializer
    return: TODO
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Post
        fields = ('id', 'title', 'description',
                  'created_at', 'tag', 'views',
                  'slug', 'owner')


class UserSerializer(serializers.ModelSerializer):
    """TODO: representing posts(jobs) owner
    return: TODO
    """
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        field = ('id', 'username', 'posts')
