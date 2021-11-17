from django import forms
from django import forms
from django.forms import widgets
from . import models


class CommentForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = (
            "comment",
        )
        labels = {
            "comment": "",
        }
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'cols': 10, 'rows': 1,
                    "placeholder": "댓글을 남겨보세요",
                }),
        }

    def save(self):
        comment = super().save(commit=False)
        return comment
