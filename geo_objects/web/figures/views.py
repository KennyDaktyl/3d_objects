from web.models.figures import Figures
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import FiguresSerializer

class FiguresViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Figures.objects.all().order_by('-created_time')
    serializer_class = FiguresSerializer
    permission_classes = [permissions.IsAuthenticated]