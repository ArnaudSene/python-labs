from rest_framework import serializers

from posts.models import BlogPost


class Serializer(serializers.HyperlinkedModelSerializer):
    """Serializer."""

    class Meta:
        """Meta."""

        model = BlogPost
        fields = ['url', 'id', 'title', 'author', 'last_updated', 'created_on',
                  'published', 'content']
