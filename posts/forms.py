from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from . import models


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = (
            "title",
            "number_of_people",
            "explain",
            "OttType",
            "pending",
        )
        labels = {
            "title": "제목",
            "number_of_people": "구하는 인원수",
            "explain": "설명창",
            "OttType": "카테고리",
            "pending": "진행여부"
        }

        widgets = {
            "OttType": forms.Select()
        }

    def clean_number_of_people(self):
        number_of_people = self.cleaned_data.get("number_of_people")

        if number_of_people < 1:
            self.add_error("number_of_people",
                           forms.ValidationError("구하는 인원 수를 1 이상으로 해주세요"))
        elif number_of_people > 8:
            self.add_error("number_of_people",
                           forms.ValidationError("구하는 인원 수를 8 이하로 해주세요"))
            # raise forms.ValidationError("에러테스트")
        else:
            return number_of_people

    # PENDING_PROCEEDING = "모집중"
    # PENDING_END = "모집완료"

    # PENDING_CHOICES = (
    #     (PENDING_PROCEEDING, "모집중"),
    #     (PENDING_END, "모집완료"),
    # )

    # title = forms.CharField(max_length=100)
    # number_of_people = forms.IntegerField()
    # explain = forms.CharField(widget=forms.Textarea)
    # OttType = forms.ModelChoiceField(
    #     queryset=models.OttType.objects.all(),
    #     widget=forms.Select(),
    # )
    # pending = forms.ChoiceField(
    #     widget=forms.Select,
    #     choices=PENDING_CHOICES,
    # )

    # def save(self):
