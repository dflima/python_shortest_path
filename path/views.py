import re
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
from .models import Graph

class PathList(APIView):

    def get(self, request, format=None):
        graph = Graph()
        graph.add_edge(0, 1);
        graph.add_edge(0, 3);
        graph.add_edge(1, 2);
        graph.add_edge(3, 4);
        graph.add_edge(3, 7);
        graph.add_edge(4, 5);
        graph.add_edge(4, 6);
        graph.add_edge(4, 7);
        graph.add_edge(5, 6);
        graph.add_edge(6, 7);

        from_node = request.query_params.get('from')
        to_node = request.query_params.get('to')

        if from_node == None or to_node == None:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)

        pattern = re.compile(r'^[A-Z]{1}$')
        if not pattern.match(from_node) or not pattern.match(to_node):
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)

        # shortest_distance = graph.shortest_distance(ord(from_node)-65, ord(to_node)-65)
        # return Response({"Path": shortest_distance}, status=status.HTTP_200_OK)
        return Response('Not implemented yet.', status=status.HTTP_501_NOT_IMPLEMENTED)


class ConnectNode(APIView):

    def post(self, request, format=None):
        return Response('Not implemented yet.', status=status.HTTP_501_NOT_IMPLEMENTED)
