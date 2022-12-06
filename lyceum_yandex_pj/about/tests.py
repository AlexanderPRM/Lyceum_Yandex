from datetime import datetime

from django.test import Client, TestCase
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch

from users.models import User


class StaticURLTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user1 = User.objects.create(
            email="mail2@mail.com",
            password="12344dre",
            birthday=datetime.today(),
        )

    def test_about(self):
        response = Client().get(reverse("about:main"))
        self.assertEqual(response.status_code, 200)

    def test_negative_about(self):
        with self.assertRaises(NoReverseMatch):
            Client().get(reverse("/negative_url_for_test"))

    def test_negative2_about(self):
        with self.assertRaises(NoReverseMatch):
            Client().get(reverse('/""'))

    def test_birthday_on_page(self):
        response = Client().get(reverse("about:main"))
        self.assertIn("birthdays", response.context)

    def test_user_in_birthday_table(self):
        response = Client().get(reverse("about:main"))
        self.assertIn(self.user1.email,
                      response.context["birthdays"][0]["email"])

    def tearDown(self):
        User.objects.all().delete()
        super().tearDown()
