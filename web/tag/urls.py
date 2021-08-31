from django.urls import path

from .views import *

urlpatterns = [
    path('', TagViewSet.as_view()),
    path('<uuid:tag_id>', TagViewDetails.as_view()),
]