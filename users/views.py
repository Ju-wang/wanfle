import os
import requests
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import request
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.core.files.base import ContentFile
from django.views.generic import View
from . import forms
from users import models as user_models
from posts import models as post_models


class LoginView(View):

    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(
                self.request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f"안녕하세요 {user.last_name}{user.first_name}님!")
                return redirect("core:home")
            else:
                return redirect("users:login")

        return render(request, "users/login.html", {"form": form})


def Logout(request):

    logout(request)
    messages.info(request, "로그아웃 되었습니다")
    return redirect("core:home")


class SignUpView(View):

    def get(self, request):
        form = forms.SignUpForm()
        return render(request, "users/signup.html", {"form": form})

    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(
                self.request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f"안녕하세요 {user.last_name}{user.first_name}님!")
                return redirect("core:home")
            else:
                return redirect("users:login")

        return render(request, "users/signup.html", {"form": form})


def kakao_login(request):

    REST_API_KEY = "1c3bae73ef442ab9039bc4b748bc7cce"
    REDIRECT_URI = "http://127.0.0.1:8000/users/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code"
    )


class KakaoException(Exception):
    pass


def kakao_callback(request):

    try:
        REST_API_KEY = "1c3bae73ef442ab9039bc4b748bc7cce"
        REDIRECT_URI = "http://127.0.0.1:8000/users/login/kakao/callback"
        code = request.GET.get("code")
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&code={code}")
        token_json = token_request.json()
        error = token_json.get("error", None)
        if error is not None:
            raise KakaoException("토큰 정보가 없습니다")
        access_token = token_json.get("access_token")
        profile_request = requests.get(
            f"https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"})
        profile_json = profile_request.json()
        email = profile_json.get("kakao_account").get("email")
        if email is None:
            raise KakaoException("카카오 이메일 제공에 동의해주세요!")
        properties = profile_json.get("properties")
        nickname = properties.get("nickname")
        profile_image = properties.get("profile_image")
        try:
            user = user_models.User.objects.get(email=email)
            if user.login_method != user_models.User.LOGIN_KAKAO:
                raise KakaoException(f"{user.login_method}로 로그인 해주세요")
        except user_models.User.DoesNotExist:
            user = user_models.User.objects.create(
                email=email,
                username=email,
                first_name=nickname,
                login_method=user_models.User.LOGIN_KAKAO,
            )
            user.set_unusable_password()
            user.save()
            if profile_image is not None:
                photo_request = requests.get("http://profile_image")
                user.avatar.save(f"{nickname}님의 프로필 사진",
                                 ContentFile(photo_request.content))
        login(request, user)
        messages.info(request, f"안녕하세요 {user.last_name}{user.first_name}님!")
        return redirect("core:home")
    except KakaoException as e:
        messages.error(request, e)
        return redirect("users:login")


@login_required
def user_profile(request, pk):

    user = get_object_or_404(user_models.User, pk=pk)

    return render(request, "users/profile.html", {"user_obj": user})


@login_required
def edit_profile(request, pk):

    user = get_object_or_404(user_models.User, pk=pk)

    if request.method == "GET":
        form = forms.EditProfile(instance=user)

    if request.method == "POST":
        form = forms.EditProfile(request.POST, instance=user)
        if form.is_valid():
            user.save()
            messages.success(
                request, "프로필이 수정되었습니다!")
            return redirect(reverse("users:profile", kwargs={"pk": pk}))

    return render(request, "users/edit_profile.html", {"user": user, "form": form})


@login_required
def change_password(request, pk):

    user = get_object_or_404(user_models.User, pk=pk)

    if request.method == "GET":
        form = forms.ChangePassword()

    if request.method == "POST":
        form = forms.ChangePassword(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get("password")
            user = get_object_or_404(user_models.User, pk=pk)
            user.set_password(new_password)
            user.save()
            messages.success(
                request, "비밀번호가 변경되었습니다!")
            login(request, user)
            return redirect(reverse("users:profile", kwargs={"pk": pk}))

    return render(request, "users/change_password.html", {"user": user, "form": form})
