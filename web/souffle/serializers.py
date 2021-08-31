from django.db.models.query import QuerySet
from web.models.tag import Tag
from web.tag.serializers import TagSerializer
from web.models import Souffle
from rest_framework import serializers


class SouffleSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Souffle
        fields = ['id', 'name', 'category', 'width', 'height', 'lon', 'lat', 'elevation', 'altitude', 'tags', 'slug']

        read_only_fields = ['id', 'tags']


class SoufflePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Souffle
        fields = ['name', 'category', 'width', 'height', 'lon', 'lat', 'elevation', 'altitude', 'tags']
        optional_fields = ['category', 'tags', ]


