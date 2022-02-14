
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """UserSerializer/"""

    class Meta:
        """Meta."""

        model = User
        exclude = ['password']
