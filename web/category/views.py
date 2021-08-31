import django_filters.rest_framework
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema

from .serializers import *
from web.models import Sphere


# class FiguresViewSet(viewsets.ModelViewSet):
class CategoryViewSet(APIView):
    """
    Return a list of all categories.
    """
    queryset = Category.objects.all()
    model = Category
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name']

    @swagger_auto_schema(
        operation_id='category_view',
        tags=['category'],
        responses={'200': CategorySerializer}
    )

    def get(self, request, format=None):
        """
        Return a list of all catogires.
        """
        categories =  Category.objects.all()
        data_out = CategorySerializer(categories, many=True)
        return Response(data_out.data)
    
    @swagger_auto_schema(
        operation_id='category_create',
        tags=['category'],
        request_body=CategoryPostSerializer,
        responses={'200': CategorySerializer}
    )

    def post(self, request, format=None):
        serializer = CategorySerializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewDetails(APIView):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = Category.objects.all()
    model = Category
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name']

    @swagger_auto_schema(
        operation_id='category_details_view',
        tags=['category'],
        responses={'200': CategorySerializer}
    )

    def get(self, request, category_id, *args, **kwargs):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id='category_update_view',
        tags=['category'],
        request_body=CategoryPostSerializer,
        responses={'200': CategorySerializer}
    )

    def put(self, request, category_id, *args, **kwargs):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_id='category_delete',
        tags=['category'],
        responses={'200': CategorySerializer}
    )

    def delete(self, request, category_id, *args, **kwargs):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
