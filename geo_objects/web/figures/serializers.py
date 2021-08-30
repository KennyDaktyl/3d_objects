from web.models import Figures, Tag
from rest_framework import serializers


class FiguresSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Figures
        fields = ['id', 'name', 'category', 'object_type', 'lon', 'lat', 'elevation', 'altitude', 'tags']


class FiguresPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Figures
        fields = ['id', 'name', 'category', 'object_type', 'lon', 'lat', 'elevation', 'altitude', 'tags']


class TagsSerializer(serializers.ModelSerializer):
    figures = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    fields = '__all__'

    class Meta:
        model = Tag