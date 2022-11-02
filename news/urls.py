from django.urls import path, include

from news.views import *

# URL = http://127.0.0.1:8000

urlpatterns = [
    # AboutService API
    path('aboutservice/', AboutServiceViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('aboutservice/<int:id>/', AboutServiceViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                                       'put': 'update', 'delete': 'destroy'})),


    # Slogan API
    path('slogan/', SloganViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('slogan/<int:id>/', SloganViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                    'put': 'update', 'delete': 'destroy'})),


    # AboutUs API
    path('aboutus/', AboutUsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('aboutus/<int:id>/', AboutUsViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'})),


    # Services API
    path('services/', ServicesViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('services/<int:id>/', ServicesViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                        'put': 'update', 'delete': 'destroy'})),


    # Features API
    path('features/', FeaturesViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('features/<int:id>/', FeaturesViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                               'put': 'update', 'delete': 'destroy'})),


    # Partners API
    path('partners/', PartnersViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('partners/<int:id>/', PartnersViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                               'put': 'update', 'delete': 'destroy'})),


    # News API
    path('news/', NewsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('news/<int:id>/', NewsViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                       'put': 'update', 'delete': 'destroy'})),


    # Contacts API
    path('contacts/', ContactsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('contacts/<int:id>/', ContactsViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                       'put': 'update', 'delete': 'destroy'})),


]
