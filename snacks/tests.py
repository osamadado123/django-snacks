from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.
class Snacks_tests(SimpleTestCase) :
    def test_home (self):
        url = reverse('home')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
    def test_about_us (self):
        url = reverse('about us')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
