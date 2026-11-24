from django.test import TestCase
from django.urls import reverse


class ListingsTests(TestCase):
    def test_listings_placeholder_response(self):
        response = self.client.get(reverse('listings_index'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Listings API is working!'})
