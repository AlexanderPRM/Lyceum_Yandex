from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from parameterized import parameterized

# from unittest.mock import patch, Mock

from datetime import datetime
from users.models import User

URLS_LIST = [
    ("about:main"),
    ("catalog:item_list"),
    ("feedback:feedback"),
    ("homepage:main"),
    ("users:register"),
]


class ContextProcessorTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        user = User.objects.create(
            email="mail2@mail.com",
            password="12344dre",
            birthday=datetime.today(),
            first_name="Андрей",
        )
        cls.user_email = user.email
        cls.user_first_name = user.first_name

    @parameterized.expand(URLS_LIST)
    def test_birthday_on_page(self, reverse_url):
        response = Client().get(reverse(reverse_url))
        self.assertIn("birthdays", response.context)

    @parameterized.expand(URLS_LIST)
    def test_birthday_length(self, reverse_url):
        response = Client().get(reverse(reverse_url))
        self.assertEqual(1, len(response.context["birthdays"]))

    @parameterized.expand(URLS_LIST)
    def test_user_in_birthdays_table(self, reverse_url):
        response = Client().get(reverse(reverse_url))
        self.assertEqual(
            self.user_email, response.context["birthdays"][0]["email"]
        )
        self.assertEqual(
            self.user_first_name,
            response.context["birthdays"][0]["first_name"],
        )

    def tearDown(self):
        User.objects.all().delete()
        super().tearDown()
