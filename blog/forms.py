from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    RATING_CHOICES = [(i, '⭐' * i) for i in range(1, 6)]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect,
        label="Avaliação"
    )

    class Meta:
        model = Post
        fields = ['title', 'artist', 'album', 'rating', 'description']
        labels = {
            'title': 'Título da Crítica',
            'artist': 'Artista',
            'album': 'Álbum',
            'description': 'Descrição',
        }
