from django.db import models

class Post(models.Model):
    title = models.CharField("Título", max_length=200)
    artist = models.CharField("Artista", max_length=100)
    album = models.CharField("Álbum", max_length=100)
    description = models.TextField("Descrição")
    rating = models.IntegerField("Nota (1–5)")
    album_cover_url = models.URLField("Capa do Álbum (URL)", blank=True, null=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    def __str__(self):
        return f"{self.title} – {self.artist}"
