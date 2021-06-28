from collections import defaultdict
from django.db import models


# Create your models here.

class Graph(models.Model):

    class Meta:

        db_table = 'graph'

    node = models.IntegerField(db_index=True)
    vertices = models.CharField(max_length=200)

    def build_graph(self):
        graph = defaultdict(list)
        nodes = Graph.objects.all()
        for node in nodes:
            vertices_list = node.vertices.split(',')
            vertices = list(map(lambda v: int(v), vertices_list))
            graph[node.node] = vertices
        return graph

    def update_vertices(self, to_node):
        if len(self.vertices) >= 1:
            self.vertices += ",{:d}".format(ord(to_node)-65)
        else:
            self.vertices = "{:d}".format(ord(to_node)-65)
