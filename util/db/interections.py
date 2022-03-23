from django.db import models
from accounts.models import CustomUser
from .base import BaseNameField


class BaseInteraction(BaseNameField):
    text = models.TextField(max_length=600)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_author",
        related_query_name="%(app_label)s_%(class)ss",
    )
    
    likes = models.ManyToManyField(
        CustomUser,
        related_name="%(app_label)s_%(class)s_like",
        related_query_name="%(app_label)s_%(class)ss",
        default=None,
        blank=True
    )
    
    @property
    def count_likes(self) -> int:
        return self.likes.count()
    
    class Meta:
        abstract = True