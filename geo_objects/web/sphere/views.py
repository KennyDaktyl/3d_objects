import django_filters.rest_framework
from rest_framework import permissions
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema

from .serializers import *
from web.models import Sphere


# class FiguresViewSet(viewsets.ModelViewSet):
class SphereViewSet(APIView):
    """
    Return a list of all spheres.
    """
    queryset = Sphere.objects.all()
    model = Sphere
    serializer_class = SphereSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['tags__slug']

    @swagger_auto_schema(
        operation_id='sphere_view',
        tags=['sphere'],
        responses={'200': SphereSerializer}
    )
    
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        spheres =  Sphere.objects.all()
        tags = self.request.query_params.get('search')
        param_list = []
        if tags:
            for el in tags.split('|'):
                param_list.append(str(el))
            spheres = spheres.filter(tags__slug__in=param_list).distinct()
        data_out = SphereSerializer(spheres, many=True)
        return Response(data_out.data)
    
    @swagger_auto_schema(
        operation_id='sphere_create',
        tags=['sphere'],
        request_body=SpherePostSerializer,
        responses={'200': SpherePostSerializer}
    )

    def post(self, request, format=None):
        serializer = SpherePostSerializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SphereViewDetails(APIView):
    """
    API endpoint that allows sphere to be viewed or edited.
    """
    queryset = Sphere.objects.all()
    model = Sphere
    serializer_class = SphereSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['tags__slug']

    @swagger_auto_schema(
        operation_id='sphere_detail_view',
        tags=['sphere'],
        responses={'200': SphereSerializer}
    )

    def get(self, request, sphere_id, *args, **kwargs):
        try:
            sphere = Sphere.objects.get(pk=sphere_id)
        except Sphere.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SpherePostSerializer(sphere)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_id='sphere_detail_update',
        tags=['sphere'],
        request_body=SpherePostSerializer,
        responses={'200': SphereSerializer}
    )

    def put(self, request, sphere_id, *args, **kwargs):
        try:
            sphere = Sphere.objects.get(pk=sphere_id)
        except Sphere.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SpherePostSerializer(sphere, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_id='sphere_delete',
        tags=['sphere'],
        responses={'200': SphereSerializer}
    )

    def delete(self, request, sphere_id, *args, **kwargs):
        try:
            sphere = Sphere.objects.get(pk=sphere_id)
        except Sphere.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        sphere.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
