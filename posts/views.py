from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, \
    DeleteView

from posts.models import BlogPost


class ListBlogPosts(ListView):
    """ListBlogPosts."""

    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)


@method_decorator(login_required, name='dispatch')
class CreateBlogPost(CreateView):
    """CreateBlogPost."""

    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ["title", "content"]


@method_decorator(login_required, name='dispatch')
class UpdateBlogPost(UpdateView):
    """UpdateBlogPost."""

    model = BlogPost
    template_name = "posts/blogpost_update.html"
    fields = ["title", "content", "published"]


class ShowBlogPost(DetailView):
    """ShowBlogPost."""

    model = BlogPost
    context_object_name = "post"
    template_name = "posts/blogpost_show.html"


@method_decorator(login_required, name='dispatch')
class DeleteBlogPost(DeleteView):
    """ShowBlogPost."""

    model = BlogPost
    context_object_name = "post"
    template_name = "posts/blogpost_delete.html"
    success_url = reverse_lazy("posts:home")
