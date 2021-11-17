from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import PasswordInput, widgets
from django.forms.fields import CharField
from users import models as user_models


class LoginForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "아이디"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호"})
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = user_models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error(
                    "password", forms.ValidationError("비밀번호가 일치하지 않습니다"))
        except user_models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("유저가 존재하지 않습니다"))


class SignUpForm(forms.Form):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "이름"}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "성"}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": "이메일"}))
    password = forms.CharField(widget=PasswordInput(
        attrs={"placeholder": "비밀번호"}))
    password1 = forms.CharField(widget=PasswordInput(
        attrs={"placeholder": "비밀번호 재입력"}))

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if len(password) <= 5:
            self.add_error("password", forms.ValidationError(
                "비밀번호를 6자리 이상 입력해주세요"))
        elif password != password1:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다")
        else:
            return password

    def clean_email(self):
        email = self.cleaned_data.get("email")

        try:
            user_models.User.objects.get(email=email)
            raise ValidationError("해당 이메일이 이미 존재합니다")
        except user_models.User.DoesNotExist:
            return email

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = user_models.User.objects.create_user(
            username=email, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()


class EditProfile(forms.ModelForm):

    class Meta:
        model = user_models.User
        fields = (
            "first_name",
            "last_name",
            # "avatar",
        )

        widgets = {
            "first_name": forms.TextInput(attrs={
                "placeholder": "이름"
            }),
            "last_name": forms.TextInput(attrs={
                "placeholder": "성"
            }),
        }


class ChangePassword(forms.Form):

    password = forms.CharField(widget=PasswordInput(attrs={
        "placeholder": "새로운 비밀번호"
    }))
    password1 = forms.CharField(widget=PasswordInput(attrs={
        "placeholder": "새로운 비밀번호 확인"
    }))

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if len(password) <= 5:
            self.add_error("password", forms.ValidationError(
                "비밀번호를 6자리 이상 입력해주세요"))
        elif password != password1:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다")
        else:
            return password
