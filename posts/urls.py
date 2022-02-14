from django.urls import path
from posts.views import ListBlogPosts, CreateBlogPost, UpdateBlogPost, \
    ShowBlogPost, DeleteBlogPost

app_name = "posts"
urlpatterns = [
    path('', ListBlogPosts.as_view(), name="home"),
    path('create/', CreateBlogPost.as_view(), name="create-post"),
    path('update/<str:slug>/', UpdateBlogPost.as_view(), name="update-post"),
    path('delete/<str:slug>/', DeleteBlogPost.as_view(), name="delete-post"),
    path('<str:slug>/', ShowBlogPost.as_view(), name="show-post"),
]
