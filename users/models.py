from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):

    LOGIN_EMAIL = "email"
    LOGIN_KAKAO = "kakao"
    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_KAKAO, "Kakao")
    )

    bio = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to="avatar")
    login_method = models.CharField(
        choices=LOGIN_CHOICES, max_length=7, blank=True, default=LOGIN_EMAIL)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def __str__(self):
        return self.username
