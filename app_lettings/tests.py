from django.test import TestCase
from django.urls import reverse

# from .models import Letting


class TestLettings(TestCase):
    # def setUp(self):
    # 	pass

    def test(self):
        response = self.client.get(reverse("lettings:index"))

        assert response.status_code == 200
        assert b"<title>Lettings</title>" in response.content
