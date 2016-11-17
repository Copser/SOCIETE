from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """TODO: def Post serializer
    return: TODO
    """
    class Meta:
        model = Post
        fields = ('id', 'title', 'description',
                  'created_at', 'tag', 'views', 'slug')


class UserSerializer(serializer.ModelSerializer):
    """TODO: representing posts(jobs) owner
    return: TODO
    """
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        field = ('id', 'username', 'posts')
