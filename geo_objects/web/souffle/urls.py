from django.urls import path
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from .views import *

urlpatterns = [
    path('', SouffleViewSet.as_view()),
    path('<uuid:souffle_id>', SouffleViewDetails.as_view()),
]