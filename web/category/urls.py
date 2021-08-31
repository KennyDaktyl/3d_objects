from django.urls import path

from .views import *

urlpatterns = [
    path('', CategoryViewSet.as_view()),
    path('<uuid:category_id>', CategoryViewDetails.as_view()),
]