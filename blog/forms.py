from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'album', 'album_cover_url', 'artist', 'rating', 'description']
        widgets = {
            'album': forms.HiddenInput(),
            'album_cover_url': forms.HiddenInput(),
            'artist': forms.HiddenInput(),
        }
