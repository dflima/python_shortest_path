import re
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

from .models import Graph
from .admin import BFS


class PathList(APIView):

    def get(self, request, format=None):
        g = Graph()
        bfs = BFS()

        graph = g.build_graph()

        from_node = request.query_params.get('from')
        to_node = request.query_params.get('to')

        if from_node == None or to_node == None:
            return Response('Bad request',
                            status=status.HTTP_400_BAD_REQUEST)

        pattern = re.compile(r'^[A-Z]{1}$')
        if not pattern.match(from_node) or not pattern.match(to_node):
            return Response('Bad request',
                            status=status.HTTP_400_BAD_REQUEST)

        shortest_distance = bfs.shortest_distance(
            graph=graph,
            source=ord(from_node)-65,
            destination=ord(to_node)-65,
        )

        return Response({'Path': shortest_distance},
                        status=status.HTTP_200_OK)


class ConnectNode(APIView):

    def post(self, request, format=None):
        from_node = request.data.get('from', '')
        to_node = request.data.get('to', '')

        pattern = re.compile(r'^[A-Z]{1}$')
        if not pattern.match(from_node) or not pattern.match(to_node):
            return Response('Bad request',
                            status=status.HTTP_400_BAD_REQUEST)

        node_from, created = Graph.objects.get_or_create(node=ord(from_node)-65)
        node_from.update_vertices(to_node)

        node_to, created = Graph.objects.get_or_create(node=ord(to_node)-65)
        node_to.update_vertices(from_node)

        try:
            node_from.save()
            node_to.save()
        except Exception as e:
            return Response('Internal Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('Created', status=status.HTTP_201_CREATED)
