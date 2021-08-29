from web.models.figures import Figures
from rest_framework import serializers


class FiguresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Figures
        fields = ['id', 'lon', 'lat',]
