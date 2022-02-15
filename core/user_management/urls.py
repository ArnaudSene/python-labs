from rest_framework import routers

from user_management.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)