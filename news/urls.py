from django.urls import path, include

from news.views import *

urlpatterns = [
    # AboutService API
    path('api/v1/aboutservice/', AboutServiceViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/aboutservice/<int:id>/', AboutServiceViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                                       'put': 'update', 'delete': 'destroy'})),

    # Features API
    path('api/v1/features/', FeaturesViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/features/<int:id>/', FeaturesViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                               'put': 'update', 'delete': 'destroy'})),

    # Features API
    path('api/v1/news/', NewsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/news/<int:id>/', NewsViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                       'put': 'update', 'delete': 'destroy'})),


]
