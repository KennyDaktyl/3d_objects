from web.models import Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')

class TagPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name',)
