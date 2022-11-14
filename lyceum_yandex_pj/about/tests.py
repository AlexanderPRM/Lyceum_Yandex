from django.test import Client, TestCase
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch


class StaticURLTest(TestCase):
    def test_about(self):
        response = Client().get(reverse('about:main'))
        self.assertEqual(response.status_code, 200)

    def test_negative_about(self):
        with self.assertRaises(NoReverseMatch):
            Client().get(reverse('/negative_url_for_test'))

    def test_negative2_about(self):
        with self.assertRaises(NoReverseMatch):
            Client().get(reverse('/""'))
