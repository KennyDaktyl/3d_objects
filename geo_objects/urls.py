# from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework import permissions

from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="3D_GeoObjects API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# router = routers.DefaultRouter()
# router.register(r'figures', FiguresViewSet)
# router.register(r'tags', TagsFilterViewSet)

# schema_view = get_schema_view(
#    openapi.Info(
#       title="3D_Figures API",
#       default_version='v1',
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/v1/category/', include('web.category.urls')),
    path('api/v1/sphere/', include('web.sphere.urls')),
    path('api/v1/souffle/', include('web.souffle.urls')),
    path('api/v1/tag/', include('web.tag.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
