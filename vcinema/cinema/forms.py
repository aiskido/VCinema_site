from .models import Comments
from django.forms import ModelForm
from django import forms


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["name", "movie", "comment"]