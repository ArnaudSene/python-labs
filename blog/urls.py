from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from posts.urls import router as posts_router
from user_management.urls import router as user_management_router

router = routers.DefaultRouter()
router.registry.extend(posts_router.registry)
router.registry.extend(user_management_router.registry)

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
    path('api/', include(router.urls), name='api'),
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('', include('posts.urls')),

]
