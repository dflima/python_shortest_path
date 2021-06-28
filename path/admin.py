from collections import defaultdict
from django.contrib import admin

# Register your models here.
class BFS:
    def add_edge(self, graph, source, destination):
        graph[source].append(destination)
        graph[destination].append(source)

    def BFS(self, graph, source, destination, predecessor, distance):
        vertices = len(graph)
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
            for i in range(len(graph[u])):
                if (visited[graph[u][i]] == False):
                    visited[graph[u][i]] = True
                    distance[graph[u][i]] = distance[u] + 1;
                    predecessor[graph[u][i]] = u
                    queue.append(graph[u][i])

                    if (graph[u][i] == destination):
                        return True
        return False

    def shortest_distance(self, graph, source, destination):
        predecessor = defaultdict(list)
        distance = defaultdict(list)

        if (self.BFS(graph, source, destination, predecessor, distance) == False):
            print("Given source and destination are not connected")
            return ""

        path = []
        crawl = destination
        path.append(crawl)

        while (predecessor[crawl] != -1):
            path.append(predecessor[crawl])
            crawl = predecessor[crawl]

        path.reverse()
        str_path = list(map(lambda i: chr(i+65), path))

        return ",".join(str_path)
