from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStempedModel):

    name = models.CharField(max_length=15)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class OttType(AbstractItem):
    pass


class Post(core_models.TimeStempedModel):
    # enum
    CATEGORY_NETFLIX = "Netflix"
    CATEGORY_WATCHA = "Watcha"
    CATEGORY_WAVE = "Wave"
    CATEGORY_TVING = "Tving"
    CATEGORY_DISNEY = "Disney plus"

    CATEGORY_CHOICES = (
        (CATEGORY_NETFLIX, "Netflix"),
        (CATEGORY_WATCHA, "Watcha"),
        (CATEGORY_WAVE, "Wave"),
        (CATEGORY_TVING, "Tving"),
        (CATEGORY_DISNEY, "Disney")
    )

    PENDING_PROCEEDING = "모집중"
    PENDING_END = "모집완료"

    PENDING_CHOICES = (
        (PENDING_PROCEEDING, "모집중"),
        (PENDING_END, "모집완료"),
    )

    title = models.CharField(max_length=50)
    number_of_people = models.IntegerField()
    explain = models.TextField()
    host = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts")
    pending = models.CharField(
        max_length=5, choices=PENDING_CHOICES, default=PENDING_PROCEEDING)
    OttType = models.ForeignKey(
        "OttType", related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
