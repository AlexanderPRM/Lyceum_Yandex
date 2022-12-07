from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

# from unittest.mock import patch, Mock

from datetime import datetime
from users.models import User


class ContextProcessorTest(TestCase):
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.user = User.objects.create(
            email="mail2@mail.com",
            password="12344dre",
            birthday=datetime.today(),
        )

    def test_birthday_on_page(self):
        response = Client().get(reverse("about:main"))
        self.assertIn("birthdays", response.context)

    def test_user_in_birthday_table(self):
        response = Client().get(reverse("about:main"))
        self.assertIsNotNone(response.context["birthdays"])
        self.assertIn(response.context["birthdays"][0], "email")
        self.assertIn(self.user1.email,
                      response.context["birthdays"][0]["email"])

    def tearDown(self):
        User.objects.all().delete()
        super().tearDown()
