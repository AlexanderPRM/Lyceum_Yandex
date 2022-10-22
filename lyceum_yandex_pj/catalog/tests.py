from django.test import TestCase, Client
from django.urls import reverse


class StaticURLTest(TestCase):
    def test_about(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_negative_about(self):
        response = Client().get('/negative_url_for_test')
        self.assertEqual(response.status_code, 404)

    def test_repath_about(self):
        response = Client().get(reverse('details', args=[200]))
        self.assertEqual(response.status_code, 200)

    def test_repath2_about(self):
        response = Client().get(reverse('details', args=[200202020]))
        self.assertEqual(response.status_code, 200)
