from django.db import models

class Post(models.Model):
    title = models.CharField("Título da Crítica", max_length=100)
    artist = models.CharField("Artista", max_length=100)
    album = models.CharField("Álbum", max_length=100)
    album_cover_url = models.URLField("URL da Capa do Álbum", blank=True, null=True)
    rating = models.IntegerField("Avaliação (1 a 5)")
    description = models.TextField("Descrição")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} – {self.artist}"
