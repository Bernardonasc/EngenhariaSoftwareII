import pytest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Category


class IntegrationTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.category = Category.objects.create(
            name="Categoria Teste", slug="categoria-teste"
        )

    def test_user_registration_and_login_flow(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "password1": "ComplexPass123!",
                "password2": "ComplexPass123!",
            },
        )
        self.assertRedirects(response, reverse("post_list"))

        login_success = self.client.login(
            username="newuser", password="ComplexPass123!"
        )
        self.assertTrue(login_success)

        response = self.client.post(
            reverse("post_create"),
            {
                "title": "Meu Primeiro Post",
                "artist": "Artista X",
                "album": "Álbum X",
                "album_cover_url": "http://img.com/capa.jpg",
                "rating": 5,
                "description": "Excelente álbum!",
                "category": self.category.id,
            },
        )
        self.assertRedirects(response, reverse("post_list"))
        self.assertEqual(Post.objects.count(), 1)

    def test_post_detail_view(self):
        post = Post.objects.create(
            title="Post Detalhe",
            artist="Artista A",
            album="Álbum A",
            album_cover_url="http://img.com/a.jpg",
            rating=4,
            description="Descrição do post",
            author=self.user,
            category=self.category,
        )
        response = self.client.get(reverse("post_detail", args=[post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.description)

    def test_post_list_by_category(self):
        Post.objects.create(
            title="Post Rock",
            artist="Artista B",
            album="Álbum B",
            album_cover_url="http://img.com/b.jpg",
            rating=3,
            description="Rock on!",
            author=self.user,
            category=self.category,
        )
        response = self.client.get(
            reverse("post_list_by_category", args=[self.category.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Post Rock")

    def test_post_list_by_author(self):
        Post.objects.create(
            title="Autor Post",
            artist="Artista C",
            album="Álbum C",
            album_cover_url="http://img.com/c.jpg",
            rating=4,
            description="Música boa!",
            author=self.user,
            category=self.category,
        )
        response = self.client.get(
            reverse("post_list_by_author", args=[self.user.username])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Autor Post")

    def test_login_required_to_create_post(self):
        response = self.client.get(reverse("post_create"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/post/new/")

    def test_invalid_registration_password_mismatch(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "userfail",
                "password1": "Senha123",
                "password2": "Senha456",
            },
        )
        self.assertEqual(User.objects.count(), 1)  # Apenas o user criado no setUp

    def test_post_creation_missing_fields(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("post_create"),
            {
                "title": "",
                "artist": "",
                "album": "",
                "album_cover_url": "",
                "rating": "",
                "description": "",
                "category": "",
            },
        )
        self.assertEqual(Post.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Este campo é obrigatório", html=False)
