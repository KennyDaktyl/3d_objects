from web.models.figures import Figures
from rest_framework import viewsets, generics, mixins, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import filters


from .serializers import FiguresSerializer

class FiguresViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Figures.objects.all()
    serializer_class = FiguresSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

   
class TagsFilterViewSet(generics.ListAPIView):

    queryset = Figures.objects.all()
    serializer_class = FiguresSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    # filter_backends = [filters.SearchFilter]

    filterset_fields = ['tags', ]

    def get_queryset(self):
        tags = self.request.query_params.get('search')
        if tags:
            param_list = []
            for el in tags.split('|'):
                param_list.append(str(el))
            return Figures.objects.filter(tags__slug__in=param_list).distinct()
        else:
            Figures.objects.all()

