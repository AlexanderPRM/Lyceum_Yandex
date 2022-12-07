from django.test import TestCase
from django.test.client import Client
from unittest.mock import patch

from django.urls import reverse
from parameterized import parameterized

from datetime import datetime
from users.models import User

from lyceum_yandex_pj.context_processor import now

URLS_LIST = [
    ("about:main"),
    ("catalog:item_list"),
    ("feedback:feedback"),
    ("homepage:main"),
    ("users:register"),
]


@patch('lyceum_yandex_pj.context_processor.now', return_value=datetime(2022, 1, 1, 14, 40, 59))
class ContextProcessorTest(TestCase):
    @classmethod
    @patch('lyceum_yandex_pj.tests.now', return_value=datetime(2022, 1, 1, 14, 40, 59))
    def setUpTestData(cls, mock):
        super(ContextProcessorTest, cls).setUpTestData()
        user = User.objects.create(
            email="mail2@mail.com",
            password="12344dre",
            birthday=now(),
            first_name="Андрей",
        )
        cls.user_email = user.email
        cls.user_first_name = user.first_name

    @parameterized.expand(URLS_LIST)
    def test_birthday_on_page(self, mock, reverse_url):
        response = Client().get(reverse(reverse_url))
        self.assertIn("birthdays", response.context)

    @parameterized.expand(URLS_LIST)
    def test_birthday_length(self, mock, reverse_url):
        response = Client().get(reverse(reverse_url))
        self.assertEqual(1, len(response.context["birthdays"]))

    @parameterized.expand(URLS_LIST)
    def test_user_in_birthdays_table(self, mock, reverse_url):
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
