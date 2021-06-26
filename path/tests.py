from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class PathIndexViewTests(TestCase):

    def test_not_implemented_yet(self):
        response = self.client.get(reverse('path:index'), {'from': 'A',
                                   'to': 'B'})
        self.assertEqual(response.status_code, 501)

    def test_bad_request_without_parameters(self):
        response = self.client.get(reverse('path:index'))
        self.assertEqual(response.status_code, 400)

    def test_bad_request_with_wrong_parameters(self):
        response = self.client.get(reverse('path:index'),
                                   {'from': 'invalid',
                                   'to': 'parameters'})
        self.assertEqual(response.status_code, 400)


class PathConnectNodeViewTests(TestCase):

    def test_not_implemented_yet(self):
        response = self.client.post(reverse('path:connect_node'),
                                    {'from': 'A', 'to': 'B'})
        self.assertEqual(response.status_code, 501)
