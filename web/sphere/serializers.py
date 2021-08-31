from web.models import Sphere
from web.tag.serializers import TagSerializer
from rest_framework import serializers


class SphereSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Sphere
        fields = ['id', 'name', 'category', 'object_type', 'radius', 'lon', 'lat', 'elevation', 'altitude', 'tags',]

class SpherePostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Sphere
        fields = ['id', 'name', 'category', 'object_type', 'radius', 'lon', 'lat', 'elevation', 'altitude', 'tags',]

