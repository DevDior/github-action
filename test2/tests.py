from rest_framework.test import APITestCase
from django.urls import reverse

class TestAPIViewTestCase(APITestCase):
    url = reverse("test:test")

    def test_invalid_get(self):
        
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)