import pytest
from django.test import TestCase
from blog.forms import PostForm
from django import forms


class FormsTest(TestCase):
    def test_post_form_contains_correct_fields(self):
        form = PostForm()
        expected_fields = [
            "title",
            "album",
            "album_cover_url",
            "artist",
            "rating",
            "description",
        ]
        assert list(form.fields.keys()) == expected_fields

    def test_post_form_hides_fields(self):
        form = PostForm()
        assert isinstance(form.fields["album"].widget, forms.HiddenInput)
        assert isinstance(form.fields["artist"].widget, forms.HiddenInput)
        assert isinstance(form.fields["album_cover_url"].widget, forms.HiddenInput)

    def test_post_form_success(self):
        data = {
            "title": "Test Title",
            "album": 1,
            "album_cover_url": "http://example.com/cover.jpg",
            "artist": 1,
            "rating": 5,
            "description": "A test description",
            "created_at": "2023-10-01T12:00:00Z",
            "user": 1,
        }
        form = PostForm(data)
        assert form.is_valid()

    def test_post_form_invalid_with_blank_data(self):
        form = PostForm({})
        assert not form.is_valid()
        assert "title" in form.errors
        assert "rating" in form.errors
        assert "description" in form.errors
