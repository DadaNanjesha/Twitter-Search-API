from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TwitterSearchListTest(APITestCase):

    def test_api_up_and_running(self):
        """
        Unittest to check API is up and running
        """
        url = reverse('TwitterSearchList')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
