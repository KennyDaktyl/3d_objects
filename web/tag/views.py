import django_filters.rest_framework
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework import filters, status
from rest_framework.response import Response

from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema

from .serializers import *
from web.models import Tag

class TagViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tag.objects.all()
    model = Tag
    serializer_class = TagSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name']

    @swagger_auto_schema(
        operation_id='tag_view',
        tags=['tag'],
        responses={'200': TagSerializer}
    )

    def get(self, request, format=None):
        """
        Return a list of all tags.
        """
        tags = Tag.objects.all()
        data_out = TagSerializer(tags, many=True)
        return Response(data_out.data)
    
    @swagger_auto_schema(
        operation_id='tag_create',
        tags=['tag'],
        request_body=TagPostSerializer,
        responses={'200': TagSerializer}
    )

    def post(self, request, format=None):
        serializer = TagSerializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagViewDetails(APIView):
    """
    API endpoint that allows tags to be viewed or edited.
    """
    queryset = Tag.objects.all()
    model = Tag
    serializer_class = TagSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name']

    @swagger_auto_schema(
        operation_id='tag_details_view',
        tags=['tag'],
        responses={'200': TagSerializer}
    )
    
    def get(self, request, tag_id, *args, **kwargs):
        try:
            tag = Tag.objects.get(pk=tag_id)
        except Tag.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TagSerializer(tag)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id='tag_details_update',
        tags=['tag'],
        request_body=TagPostSerializer,
        responses={'200': TagSerializer}
    )

    def put(self, request, tag_id, *args, **kwargs):
        try:
            tag = Tag.objects.get(pk=tag_id)
        except Tag.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_id='tag_details_delete',
        tags=['tag'],
        
        responses={'200': TagSerializer}
    )

    def delete(self, request, tag_id, *args, **kwargs):
        try:
            tag = Tag.objects.get(pk=tag_id)
        except Tag.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
