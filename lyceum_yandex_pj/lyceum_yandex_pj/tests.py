#  @classmethod
#     def setUpClass(cls) -> None:
#         super().setUpClass()
#         cls.user1 = User.objects.create(
#             email="mail2@mail.com",
#             password="12344dre",
#             birthday=datetime.today(),
#         )
#          def test_birthday_on_page(self):
#         response = Client().get(reverse("about:main"))
#         self.assertIn("birthdays", response.context)

#     def test_user_in_birthday_table(self):
#         response = Client().get(reverse("about:main"))
#         self.assertIn(self.user1.email,
#                       response.context["birthdays"][0]["email"])

#     def tearDown(self):
#         User.objects.all().delete()
#         super().tearDown()
