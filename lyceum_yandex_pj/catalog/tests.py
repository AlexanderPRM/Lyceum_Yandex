from catalog.models import Category, Item, Tag
from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch


class PagesURLTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.category = Category.objects.create(
                            name='Тестовая Категория',
                            slug='test',
                            weight=10)
        cls.tag = Tag.objects.create(
                    name='Тестовый тег',
                    slug='tag'
                    )
        cls.item = Item.objects.create(
                        name='Тест',
                        text='превосходно',
                        category=cls.category
                        )
        cls.item = Item.objects.create(
                        name='Тест2',
                        text='превосходно 2',
                        category=cls.category
                        )
        cls.item = Item.objects.create(
                        name='На главной',
                        text='превосходно',
                        category=cls.category,
                        is_on_main=True
                        )

    def test_catalog_detail(self):
        response = Client().get(reverse(
                                'catalog:item_detail',
                                kwargs={'pk': 1}))
        self.assertIsNotNone(response.context['item'])
        self.assertEqual(response.status_code, 200)

    def test_catalog_detail1(self):
        response = Client().get(reverse(
                                'catalog:item_detail',
                                kwargs={'pk': 2}))
        self.assertIsNotNone(response.context['item'])
        self.assertEqual(response.status_code, 200)

    def test_catalog_list(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertIsNotNone(response.context['items'])
        self.assertEqual(response.status_code, 200)

    def test_homepage_main(self):
        response = Client().get(reverse('homepage:main'))
        self.assertIsNotNone(response.context['items'])
        self.assertEqual(response.status_code, 200)

    def test_negative4_catalog(self):
        with self.assertRaises(NoReverseMatch):
            Client().get(reverse('catalog:item_detail', kwargs={'pk': -200}))

    def test_negative5_catalog(self):
        with self.assertRaises(NoReverseMatch):
            Client().get(reverse('catalog:item_detail', kwargs={'pk': 0}))


class ModelsTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.category = Category.objects.create(
                            name='Тестовая Категория',
                            slug='test',
                            weight=10)
        cls.tag = Tag.objects.create(
                    name='Тестовый тег',
                    slug='tag'
                    )

    def test_category_negative(self):
        category_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            self.category = Category(
                                name='Тестовая Категория',
                                slug='test-2',
                                weight=-10)
            self.category.full_clean()
            self.category.save()
        self.assertEqual(Category.objects.count(), category_count)

    def test_category_negative2(self):
        category_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            self.category = Category(
                                name='Тестовая Категория',
                                slug='test-2',
                                weight=40000)
            self.category.full_clean()
            self.category.save()
        self.assertEqual(Category.objects.count(), category_count)

    def test_category_negative_slug(self):
        category_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            self.category = Category(
                                name='Тестовая Категория',
                                slug='test-2//[]__--',
                                weight=10)
            self.category.full_clean()
            self.category.save()
        self.assertEqual(Category.objects.count(), category_count)

    def test_category_positive(self):
        category_count = Category.objects.count()
        self.category = Category(
                            name='Тестовая Категория',
                            slug='test-3',
                            weight=10)
        self.category.full_clean()
        self.category.save()
        self.assertEqual(Category.objects.count(), category_count + 1)

    def test_item_positive(self):
        item_count = Item.objects.count()
        self.item = Item(
                        name='Тестовое название',
                        text='превосходно',
                        category=self.category,
        )
        self.item.full_clean()
        self.item.save()
        self.item.tag.add(self.tag)
        self.assertEqual(Item.objects.count(), item_count + 1)

    def test_item_positive2(self):
        item_count = Item.objects.count()
        self.item = Item(
                        name='Тестовое название',
                        text='роскошно',
                        category=self.category,
        )
        self.item.full_clean()
        self.item.save()
        self.item.tag.add(self.tag)
        self.assertEqual(Item.objects.count(), item_count + 1)

    def test_item_negative(self):
        item_count = Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = Item(
                            name='Тестовое название',
                            text='Негативное описание',
                            category=self.category,
            )
            self.item.full_clean()
            self.item.save()
            self.item.tag.add(self.tag)
        self.assertEqual(Item.objects.count(), item_count)

    def test_tag_positive(self):
        tag_count = Tag.objects.count()
        self.tag = Tag(
                        name='Тестовый тег',
                        slug='test')
        self.tag.full_clean()
        self.tag.save()
        self.assertEqual(Tag.objects.count(), tag_count + 1)

    def test_tag_negative(self):
        tag_count = Tag.objects.count()
        with self.assertRaises(ValidationError):
            self.tag = Tag(
                            name='Тестовый тег',
                            slug='test33/21[]__--')
            self.tag.full_clean()
            self.tag.save()
        self.assertEqual(Tag.objects.count(), tag_count)
