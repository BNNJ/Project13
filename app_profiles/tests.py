from django.test import TestCase
from django.urls import reverse

# from django.contrib.auth.models import User
# from .models import Profile


class TestProfiles(TestCase):
    # def setUp(self):
    # 	pass

    def test(self):
        response = self.client.get(reverse("profiles:index"))

        assert response.status_code == 200
        assert b"<title>Profiles</title>" in response.content
