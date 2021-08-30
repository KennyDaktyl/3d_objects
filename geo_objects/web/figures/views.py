import django_filters.rest_framework
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework import filters, status
from rest_framework.response import Response

from django.http import JsonResponse

from .serializers import *
from web.models.figures import Figures


# class FiguresViewSet(viewsets.ModelViewSet):
class FiguresViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Figures.objects.all()
    model = Figures
    serializer_class = FiguresSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['tags__slug']

    
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        tags = self.request.query_params.get('search')
        param_list = []
        if tags:
            for el in tags.split('|'):
                param_list.append(str(el))
            figures = Figures.objects.filter(tags__slug__in=param_list).distinct()
            data_out = FiguresSerializer(figures, many=True)
            return Response(data_out.data)
        else:
            figures =  Figures.objects.all()
            data_out = FiguresSerializer(figures, many=True)
            return Response(data_out.data)
    
    def post(self, request, format=None):
        serializer = FiguresPostSerializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FiguresDetailView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Figures.objects.all()
    model = Figures
    serializer_class = FiguresSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['tags__slug']


    def put(self, request, figure_id, *args, **kwargs):
        try:
            figure = Figures.objects.get(pk=figure_id)
        except Figures.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FiguresPostSerializer(figure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       
    def delete(self, request, figure_id, *args, **kwargs):
        try:
            figure = Figures.objects.get(pk=figure_id)
        except Figures.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        figure.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   
class TagsFilterViewSet(generics.ListAPIView):

    queryset = Figures.objects.all()
    serializer_class = FiguresSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    # filter_backends = [filters.SearchFilter]
    filterset_fields = ['tags', ]

    def get_queryset(self):
        tags = self.request.query_params.get('search')
        if tags:
            param_list = []
            for el in tags.split('|'):
                param_list.append(str(el))
            return Figures.objects.filter(tags__slug__in=param_list).distinct()
        else:
            Figures.objects.all()


