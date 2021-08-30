from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

from .views import *


# router = routers.DefaultRouter()
# router.register(r'', FiguresViewSet.as_view({'get': 'list'}), basename='figures')

from .views import *

urlpatterns = [
    # path('figures', include(router.urls)),
    path('figures', FiguresViewSet.as_view()),
    path('figures/<uuid:figure_id>', FiguresDetailView.as_view()),
    path('tags/', TagsFilterViewSet.as_view()),
]