from rest_framework import routers
from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

from web.figures.views import FiguresViewSet, TagsFilterViewSet

# router = routers.DefaultRouter()
# router.register(r'figures', FiguresViewSet)
# router.register(r'tags', TagsFilterViewSet)

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
    path('figures/', FiguresViewSet.as_view({'get': 'list'})),
    path('tags/', TagsFilterViewSet.as_view())
]
