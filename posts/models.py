from typing import Optional

from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()


class BlogPost(models.Model):
    """New BlogPost model."""

    title = models.CharField(max_length=255, unique=True, verbose_name="Title")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Published")
    content = models.TextField(blank=True, verbose_name="Content")

    class Meta:
        """
        Override Meta class.

        ordering: ordering on field created_on
        verbose_name: Application name is Article
        """

        ordering = ['-created_on']
        verbose_name = 'Post'

    def __str__(self):
        """Display title in Django admin."""
        return self.title

    def save(self, *args, **kwargs):
        """Create a slug with slugify based on title."""
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    @property
    def author_or_default(self) -> str:
        """Get author or return unknown."""
        return self.author.username if self.author else "unknown"

    @staticmethod
    def get_absolute_url() -> Optional[str]:
        """
        Get the absolute url for redirection.

        see: posts.urls.py
        app_name:name

        """
        return reverse("posts:home")
