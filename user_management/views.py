from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user_management.serializers import UserSerializer


class MeViewSet(viewsets.ViewSet):
    """MeViewSet."""

    permission_classes = (IsAuthenticated, )

    @staticmethod
    def list(request):
        """List users."""
        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user).data
        return Response(user_data)
