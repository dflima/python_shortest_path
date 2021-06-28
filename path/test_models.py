from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch

from .models import Graph

class GraphModelTests(TestCase):

    def create_graph(self, node=0, vertices='1,2'):
        return Graph.objects.create(node=node, vertices=vertices)

    def test_graph_creation(self):
        graph = self.create_graph()
        self.assertTrue(isinstance(graph, Graph))
        self.assertEqual(0, graph.node)
        self.assertEqual('1,2', graph.vertices)


    def test_build_graph(self):
        a = self.create_graph(node=0, vertices='1')
        b = self.create_graph(node=1, vertices='1,2')
        c = self.create_graph(node=2, vertices='1')

        graph = a.build_graph()

        self.assertEqual([1], graph[a.node])
        self.assertEqual([1, 2], graph[b.node])
        self.assertEqual([1], graph[c.node])

    def test_update_vertices(self):
        graph = self.create_graph()
        graph.update_vertices('D')

        self.assertEqual('1,2,3', graph.vertices)
