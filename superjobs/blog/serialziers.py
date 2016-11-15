from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """TODO: def Post serializer
    return: TODO
    """
    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'description',
                  'created_at', 'tag', 'views', 'slug')
