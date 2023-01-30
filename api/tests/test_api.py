from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class APITests(APITestCase):

    def test_create_code_with_wrong_url(self):
        data = {"url": "wrong_url"}
        url = reverse("api_url")
        response = self.client.post(url, data, format='json')
        expected_data = {
            "pk": 1,
            "url": "wrong_url",
            "usage_counter": 0
        }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"url": ["Enter a valid URL."]})


    def test_create_code(self):
        data = {"url": "http://url.org"}
        url = reverse("api_url")
        response = self.client.post(url, data, format='json')
        expected_data = {
            "pk": 1,
            "url": "http://url.org",
            "usage_counter": 0
        }

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["pk"], expected_data["pk"])
        self.assertEqual(response.json()["url"], expected_data["url"])
        self.assertEqual(response.json()["usage_counter"], expected_data["usage_counter"])
        self.assertIsNotNone(response.json()["code"])


    def test_statistic(self):
        data = {"url": "http://url.org"}
        url = reverse("api_url")
        self.client.post(url, data, format='json')

        response = self.client.get(url, format='json')
        expected_data = {
            "pk": 2,
            "url": "http://url.org",
            "usage_counter": 0
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]["pk"], expected_data["pk"])
        self.assertEqual(response.json()[0]["url"], expected_data["url"])
        self.assertEqual(response.json()[0]["usage_counter"], expected_data["usage_counter"])
        self.assertIsNotNone(response.json()[0]["code"])
