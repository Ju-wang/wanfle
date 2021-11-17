from django.db import models


class TimeStempedModel(models.Model):

    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
