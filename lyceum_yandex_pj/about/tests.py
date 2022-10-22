from django.test import TestCase, Client


class StaticURLTest(TestCase):
    def test_about(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_negative_about(self):
        response = Client().get('/negative_url_for_test')
        self.assertEqual(response.status_code, 404)

    def test_negative2_about(self):
        response = Client().get('/""')
        self.assertEqual(response.status_code, 404)
