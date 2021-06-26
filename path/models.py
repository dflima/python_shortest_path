from collections import defaultdict
from django.db import models

# Create your models here.
class Graph(models.Model):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, source, destination):
        self.graph[source].append(destination)
        self.graph[destination].append(source)

    def BFS(self, source, destination, predecessor, distance):
        vertices = len(self.graph)
        queue = []
        visited = [False for i in range(vertices)]

        for i in range(vertices):
            distance[i] = 1000000
            predecessor[i] = -1

        visited[source] = True
        distance[source] = 0
        queue.append(source)

        while (len(queue) != 0):
            u = queue[0];
            queue.pop(0);
            for i in range(len(self.graph[u])):
                if (visited[self.graph[u][i]] == False):
                    visited[self.graph[u][i]] = True
                    distance[self.graph[u][i]] = distance[u] + 1;
                    predecessor[self.graph[u][i]] = u
                    queue.append(self.graph[u][i])

                    if (self.graph[u][i] == destination):
                        return True
        return False

    def shortest_distance(self, s, destination):
        predecessor = defaultdict(list)
        distance = defaultdict(list)

        if (self.BFS(s, destination, predecessor, distance) == False):
            print("Given source and destination are not connected")
            return ""

        path = []
        crawl = destination
        path.append(crawl)

        while (predecessor[crawl] != -1):
            path.append(predecessor[crawl])
            crawl = predecessor[crawl]

        path.reverse()
        str_path = [str(i) for i in path]

        return ",".join(str_path)
