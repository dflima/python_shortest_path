import re
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

from .models import Graph
from .admin import BFS
from .errors import BadRequestError


def validate_input(from_node, to_node):
    pattern = re.compile(r'^[A-Z]{1}$')
    if not pattern.match(from_node) or not pattern.match(to_node):
        raise BadRequestError

class PathList(APIView):

    def get(self, request, format=None):
        g = Graph()
        bfs = BFS()

        graph = g.build_graph()

        try:
            from_node = request.query_params.get('from', '')
            to_node = request.query_params.get('to', '')
            validate_input(from_node, to_node)

            shortest_distance = bfs.shortest_distance(
                graph=graph,
                source=ord(from_node)-65,
                destination=ord(to_node)-65,
            )
        except BadRequestError:
            return Response('Bad request',
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {'Path': self.format_shortest_distance(shortest_distance)},
                status=status.HTTP_200_OK
            )

    def format_shortest_distance(self, shortest_distance):
        path = list(map(lambda i: chr(i+65), shortest_distance))
        return ",".join(path)


class ConnectNode(APIView):

    def post(self, request, format=None):
        try:
            from_node = request.data.get('from', '')
            to_node = request.data.get('to', '')
            validate_input(from_node, to_node)

            node_from, created = Graph.objects.get_or_create(node=ord(from_node)-65)
            node_from.update_vertices(to_node)

            node_to, created = Graph.objects.get_or_create(node=ord(to_node)-65)
            node_to.update_vertices(from_node)

            node_from.save()
            node_to.save()
        except BadRequestError:
            return Response('Bad request',
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response('Internal Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('Created', status=status.HTTP_201_CREATED)
