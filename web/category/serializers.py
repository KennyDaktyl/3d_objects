from web.models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class CategoryPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['name']


