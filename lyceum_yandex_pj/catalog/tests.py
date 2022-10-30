from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from catalog.models import Category, Item, Tag


class StaticURLTest(TestCase):
    def test_catalog(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_negative_catalog(self):
        response = Client().get('/negative_url_for_test/')
        self.assertEqual(response.status_code, 404)

    def test_repath1_catalog(self):
        response = Client().get('/catalog/200/')
        self.assertEqual(response.status_code, 200)

    def test_repath_catalog(self):
        response = Client().get('/catalog/100/')
        self.assertEqual(response.status_code, 200)

    def test_negative4_catalog(self):
        response = Client().get('/catalog/-200/')
        self.assertEqual(response.status_code, 404)

    def test_negative5_catalog(self):
        response = Client().get('/catalog/0/')
        self.assertEqual(response.status_code, 404)


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
