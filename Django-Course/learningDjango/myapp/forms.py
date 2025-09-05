# CREAMOS LOS FORMULARIOS
from django import forms
from django.core import validators
from .models import Article


class FormArticle(forms.ModelForm):
    title = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={"placeholder": "Introduce a title"}),
        validators=[
            validators.MinLengthValidator(4, "Title too short"),
            validators.RegexValidator(
                "^[A-Za-z0-9 ]*$", "bad format tittle", "invalid_title"
            ),
        ],
    )
    content = forms.CharField(
        required=False,
        widget=forms.Textarea,
        validators=[validators.MaxLengthValidator(20, "Too much text")],
    )

    class Meta:
        model = Article
        fields = ["title", "content", "public"]
        widgets = {"public": forms.Select(choices=[(1, "Yes"), (0, "No")])}
