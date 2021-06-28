from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch


# Create your tests here.

def mocked_graph(graph):
    return {
        0: [1, 3],
        1: [0, 2],
        2: [1],
        3: [0, 4, 7],
        4: [3, 5, 6, 7],
        5: [4, 6],
        6: [4, 5, 7],
        7: [3, 4, 6],
        8: [9],
        9: [10],
        }


def simple_graph(graph):
    return {0: [1], 1: [0, 2], 2: [1]}


def disconnected_graph(graph):
    return {0: [1], 1: [0], 2: [1]}


class PathIndexViewTests(TestCase):

    @patch('path.models.Graph.build_graph', simple_graph)
    def test_return_the_shortest_path_simple_graph(self):
        response = self.client.get(reverse('path:index'), {'from': 'A',
                                   'to': 'C'})
        self.assertEqual(response.data, {'Path': 'A,B,C'})
        self.assertEqual(response.status_code, 200)

    @patch('path.models.Graph.build_graph', mocked_graph)
    def test_return_the_shortest_path_mocked_graph(self):
        response = self.client.get(reverse('path:index'), {'from': 'A',
                                   'to': 'H'})
        self.assertEqual(response.data, {'Path': 'A,D,H'})
        self.assertEqual(response.status_code, 200)

    @patch('path.models.Graph.build_graph', disconnected_graph)
    def test_empty_path_for_disconnected_nodes(self):
        response = self.client.get(reverse('path:index'), {'from': 'A',
                                   'to': 'C'})
        self.assertEqual(response.data, {'Path': ''})
        self.assertEqual(response.status_code, 200)

    def test_bad_request_without_parameters(self):
        response = self.client.get(reverse('path:index'))
        self.assertEqual(response.status_code, 400)

    def test_bad_request_with_wrong_parameters(self):
        response = self.client.get(reverse('path:index'),
                                   {'from': 'invalid',
                                   'to': 'parameters'})
        self.assertEqual(response.status_code, 400)


class PathConnectNodeViewTests(TestCase):

    def test_create_connection_between_two_nodes(self):
        response = self.client.post(reverse('path:connect_node'),
                                    {'from': 'A', 'to': 'B'})
        self.assertEqual(response.status_code, 201)

    def test_bad_request_without_parameters(self):
        response = self.client.post(reverse('path:connect_node'))
        self.assertEqual(response.status_code, 400)
