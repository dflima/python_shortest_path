from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class PathIndexViewTests(TestCase):
    def test_not_implemented_yet(self):
        response = self.client.get(reverse('path:index'))
        self.assertEqual(response.status_code, 501)

class PathConnectNodeViewTests(TestCase):
    def test_not_implemented_yet(self):
        response = self.client.get(reverse('path:connect_node'))
        self.assertEqual(response.status_code, 501)
