from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    album_cover_url = forms.URLField(widget=forms.HiddenInput())

    class Meta:
        model = Post
        fields = [
            "title",
            "album",
            "album_cover_url",
            "artist",
            "rating",
            "description",
            "category",
        ]
        widgets = {
            "album": forms.HiddenInput(),
            "album_cover_url": forms.HiddenInput(),
            "artist": forms.HiddenInput(),
        }
