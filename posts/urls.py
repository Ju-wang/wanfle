from django.urls import path
from posts import views as post_views

app_name = "posts"

urlpatterns = [
    path("list/", post_views.List, name="list"),
    path("<int:pk>/", post_views.Detail, name="detail"),
    path("<int:pk>/edit/", post_views.Edit_post, name="edit"),
    path("<int:pk>/delete/", post_views.Delete, name="delete"),
    path("create/", post_views.Create_post, name="create"),
]
