from django.urls import path

from .views import *

urlpatterns = [
    path('', SphereViewSet.as_view()),
    path('<uuid:sphere_id>', SphereViewDetails.as_view()),
]