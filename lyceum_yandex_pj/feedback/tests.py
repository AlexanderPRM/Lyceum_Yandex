from django.test import TestCase, Client
from django.urls import reverse

from feedback.forms import FeedBackForm
from feedback.models import FeedBack


class FeedbackTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.form = FeedBackForm()

    def test_context(self):
        response = Client().get(reverse("feedback:feedback"))
        self.assertIn("form", response.context)

    def test_label_mail_name(self):
        mail_name = FeedbackTests.form.fields["mail"].label
        self.assertEqual(mail_name, "Почта")

    def test_help_text_mail(self):
        mail_name = FeedbackTests.form.fields["mail"].help_text
        self.assertEqual(mail_name, "Введите вашу почту.")

    def test_label_text_name(self):
        mail_name = FeedbackTests.form.fields["text"].label
        self.assertEqual(mail_name, "Содержимое")

    def test_help_text_text(self):
        mail_name = FeedbackTests.form.fields["text"].help_text
        self.assertEqual(mail_name, "В этом поле введите текст своего обращения.")

    def test_redirect(self):
        items_count = FeedBack.objects.count()

        post = {"text": "Test text", "mail": "test@yandex.ru"}
        response = Client().post(reverse("feedback:feedback"), data=post, follow=True)
        self.assertRedirects(response, reverse("feedback:feedback"))
        self.assertEqual(items_count + 1, FeedBack.objects.count())
