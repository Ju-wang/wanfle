from django.db import models
from django.urls import reverse
from core import models as core_models


class Comment(core_models.TimeStempedModel):

    comment = models.TextField(max_length=1000)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.comment}"
