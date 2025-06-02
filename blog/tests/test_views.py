from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post


class ViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="12345")
        self.post = Post.objects.create(
            title="Test Title",
            artist="Test Artist",
            album="Test Album",
            album_cover_url="https://example.com/cover.jpg",
            rating=5,
            description="Test description",
            author=self.user,
        )

    def test_post_list(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Title")

    def test_post_detail(self):
        response = self.client.get(reverse("post_detail", args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.description)

    def test_post_create_requires_login(self):
        response = self.client.get(reverse("post_create"))
        self.assertEqual(response.status_code, 302)  # Redireciona para login
        self.assertRedirects(response, "/login/?next=/post/new/")

    def test_post_create_success(self):
        self.client.login(username="test", password="12345")
        response = self.client.post(
            reverse("post_create"),
            {
                "title": "New Post",
                "artist": "New Artist",
                "album": "New Album",
                "album_cover_url": "https://example.com/new.jpg",
                "rating": 4,
                "description": "New description",
            },
        )
        self.assertEqual(Post.objects.count(), 2)
        self.assertRedirects(response, reverse("post_list"))

    def test_post_list_by_author(self):
        response = self.client.get(
            reverse("post_list_by_author", args=[self.user.username])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Title")

    def test_register_view(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "password1": "complexpass123",
                "password2": "complexpass123",
            },
        )
        self.assertEqual(User.objects.count(), 2)  # original + new
        self.assertRedirects(response, reverse("post_list"))
