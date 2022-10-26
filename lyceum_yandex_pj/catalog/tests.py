from django.test import TestCase, Client
from django.urls import reverse


class StaticURLTest(TestCase):
    def test_catalog(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_negative_catalog(self):
        response = Client().get('/negative_url_for_test/')
        self.assertEqual(response.status_code, 404)
    
    def test_negative2_catalog(self):
        response = Client().get('/catalog/200/')
        self.assertEqual(response.status_code, 200)
    
    def test_negative2_catalog(self):
        response = Client().get('/catalog/100/')
        self.assertEqual(response.status_code, 200)
    
    def test_negative2_catalog(self):
        response = Client().get('/catalog/-200/')
        self.assertEqual(response.status_code, 404)
    
    def test_negative2_catalog(self):
        response = Client().get('/catalog/0/')
        self.assertEqual(response.status_code, 404)
    
        
