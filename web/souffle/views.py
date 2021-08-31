import django_filters.rest_framework
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework import filters, status
from rest_framework.response import Response

from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema

from .serializers import *
from web.models import Souffle


# class FiguresViewSet(viewsets.ModelViewSet):
class SouffleViewSet(APIView):
    """
    API endpoint that allows souffles to be viewed or edited.
    """
    queryset = Souffle.objects.all()
    model = Souffle
    serializer_class = SouffleSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['tags__slug']

    @swagger_auto_schema(
        operation_id='souffle_view',
        tags=['souffle'],
        responses={'200': SouffleSerializer}
    )

    def get(self, request, format=None):
        """
        Return a list of all souffles.
        """
        souffles =  Souffle.objects.all()
        tags = self.request.query_params.get('search')
        param_list = []
        if tags:
            print(tags)
            for el in tags.split('|'):
                param_list.append(str(el))
            souffles = souffles.filter(tags__slug__in=param_list).distinct()
        data_out = SouffleSerializer(souffles, many=True)
        return Response(data_out.data)
    
    @swagger_auto_schema(
        operation_id='souffle_create',
        tags=['souffle'],
        request_body=SoufflePostSerializer,
        responses={'200': SouffleSerializer}
    )
    
    def post(self, request, format=None):
        serializer = SoufflePostSerializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SouffleViewDetails(APIView):
    """
    API endpoint that allows souffle to be viewed or edited.
    """
    queryset = Souffle.objects.all()
    model = Souffle
    serializer_class = SouffleSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['tags__slug']

    @swagger_auto_schema(
        operation_id='souffle_details_view',
        tags=['souffle'],
        responses={'200': SouffleSerializer}
    )

    def get(self, request, souffle_id, *args, **kwargs):
        try:
            souffle = Souffle.objects.get(pk=souffle_id)
        except Souffle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SoufflePostSerializer(souffle)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id='souffle_update_view',
        tags=['souffle'],
        request_body=SoufflePostSerializer,
        responses={'200': SouffleSerializer}
    )

    def put(self, request, souffle_id, *args, **kwargs):
        try:
            souffle = Souffle.objects.get(pk=souffle_id)
        except Souffle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SoufflePostSerializer(souffle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_id='souffle_delete',
        tags=['souffle'],
        responses={'200': SouffleSerializer}
    )
       
    def delete(self, request, souffle_id, *args, **kwargs):
        try:
            souffle = Souffle.objects.get(pk=souffle_id)
        except Souffle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        souffle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

