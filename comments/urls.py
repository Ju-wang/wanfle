from django.urls import path
from comments import views as comment_views

app_name = "comments"

urlpatterns = [
    path("create/<int:post>/", comment_views.create_comment, name="create"),
    path("<int:post>/delete/<int:comment>/",
         comment_views.delete_comment, name="delete"),
]
