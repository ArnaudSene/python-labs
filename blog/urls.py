from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from posts.urls import router as posts_router
from user_management.urls import router as user_management_router

router = routers.DefaultRouter()
router.registry.extend(posts_router.registry)
router.registry.extend(user_management_router.registry)

urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('', include('posts.urls')),
]
