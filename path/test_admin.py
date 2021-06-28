from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch

from .admin import BFS

class BFSTests(TestCase):

    def test_shortest_distance(self):
        graph = self.mocked_graph()
        bfs = BFS()

        shortest_distance = bfs.shortest_distance(graph, 0, 7)
        self.assertEqual([0, 3, 7], shortest_distance)

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
