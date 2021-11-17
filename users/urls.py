from django.urls import path
from users import views as user_views

app_name = "users"

# 프로파일만들기

urlpatterns = [
    path("login/", user_views.LoginView.as_view(), name="login"),
    path("login/kakao/", user_views.kakao_login, name="kakao_login"),
    path("login/kakao/callback/", user_views.kakao_callback, name="kakao_callback"),
    path("logout/", user_views.Logout, name="logout"),
    path("signup/", user_views.SignUpView.as_view(), name="signup"),
    path("<int:pk>/", user_views.user_profile, name="profile"),
    path("<int:pk>/edit/profile/", user_views.edit_profile, name="edit_profile"),
    path("<int:pk>/change/password/",
         user_views.change_password, name="change_password"),
]
