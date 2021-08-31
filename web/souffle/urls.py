from django.urls import path

from .views import *

urlpatterns = [
    path('', SouffleViewSet.as_view()),
    path('<uuid:souffle_id>', SouffleViewDetails.as_view()),
]
