from django.urls import reverse

from rest_framework.test import APITestCase


class TestAPIViewTestCase(APITestCase):
    get_url = reverse("test:test")
    post_url = reverse("test:test")
    
    def test_invalid_post(self):
        print(self.get_url)
        print(self.post_url)
        
        response = self.client.post(self.post_url, {"post":True}, format='json')
        print(response)
        print(response.data)
        
        self.assertEqual(400, response.status_code)
        self.assertEqual(True, response.data['results'])
        self.assertTrue(response.data['results'])