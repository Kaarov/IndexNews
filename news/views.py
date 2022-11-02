# from django.shortcuts import render
from rest_framework.permissions import BasePermission, AllowAny, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from news.models import *
from news.serializers import *


# Rest Api

# ---------

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


# AboutService
class AboutServiceViewSet(ModelViewSet):
    serializer_class = AboutServiceSerializer
    queryset = AboutService.objects.all()
    permission_classes = [ReadOnly]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny | ReadOnly]
        elif self.action in ['list', 'retrieve', 'create', 'update']:
            self.permission_classes = [ReadOnly]
        else:
            self.permission_classes = [ReadOnly]
        return super(AboutServiceViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = AboutService.objects.all()
        serializer = AboutServiceSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        check = AboutService.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = AboutService.objects.get(pk=kwargs.get('id'))
            serializer = AboutServiceSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        check = AboutService.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = AboutService.objects.get(pk=kwargs.get('id'))
            serializer = AboutServiceSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        check = AboutService.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = AboutService.objects.get(pk=kwargs.get('id'))
            self.perform_destroy(instance)
        else:
            return Response("error: Not found", status=200)
        return Response("success: Destroyed", status=200)


# ---------


# SLogan / Slogan Items
class SloganViewSet(ModelViewSet):
    serializer_class = SloganSerializer
    queryset = Slogan.objects.all()
    permission_classes = [ReadOnly]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny | ReadOnly]
        elif self.action in ['list', 'retrieve', 'create', 'update']:
            self.permission_classes = [ReadOnly]
        else:
            self.permission_classes = [ReadOnly]
        return super(SloganViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = Slogan.objects.all()
        serializer = SloganSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        check = Slogan.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Slogan.objects.get(pk=kwargs.get('id'))
            serializer = SloganSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        check = Slogan.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Slogan.objects.get(pk=kwargs.get('id'))
            serializer = SloganSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        check = Slogan.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Slogan.objects.get(pk=kwargs.get('id'))
            self.perform_destroy(instance)
        else:
            return Response("error: Not found", status=200)
        return Response("success: Destroyed", status=200)


# ---------


# AboutUs / About Us Items
class AboutUsViewSet(ModelViewSet):
    serializer_class = AboutUsSerializer
    queryset = AboutUs.objects.all()
    permission_classes = [ReadOnly]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny | ReadOnly]
        elif self.action in ['list', 'retrieve', 'create', 'update']:
            self.permission_classes = [ReadOnly]
        else:
            self.permission_classes = [ReadOnly]
        return super(AboutUsViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = AboutUs.objects.all()
        serializer = AboutUsSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        check = AboutUs.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = AboutUs.objects.get(pk=kwargs.get('id'))
            serializer = AboutUsSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        check = AboutUs.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = AboutUs.objects.get(pk=kwargs.get('id'))
            serializer = AboutUsSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        check = AboutUs.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = AboutUs.objects.get(pk=kwargs.get('id'))
            self.perform_destroy(instance)
        else:
            return Response("error: Not found", status=200)
        return Response("success: Destroyed", status=200)


# ---------


# Services / Services Items
class ServicesViewSet(ModelViewSet):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()
    permission_classes = [ReadOnly]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny | ReadOnly]
        elif self.action in ['list', 'retrieve', 'create', 'update']:
            self.permission_classes = [ReadOnly]
        else:
            self.permission_classes = [ReadOnly]
        return super(ServicesViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = Services.objects.all()
        serializer = ServicesSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        check = Services.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Services.objects.get(pk=kwargs.get('id'))
            serializer = ServicesSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        check = Services.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Services.objects.get(pk=kwargs.get('id'))
            serializer = ServicesSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        check = Services.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Services.objects.get(pk=kwargs.get('id'))
            self.perform_destroy(instance)
        else:
            return Response("error: Not found", status=200)
        return Response("success: Destroyed", status=200)


# ---------

# Features
class FeaturesViewSet(ModelViewSet):
    serializer_class = FeaturesSerializer
    queryset = Features.objects.all()
    permission_classes = [ReadOnly]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny | ReadOnly]
        elif self.action in ['list', 'retrieve', 'create', 'update']:
            self.permission_classes = [ReadOnly]
        else:
            self.permission_classes = [ReadOnly]
        return super(FeaturesViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = Features.objects.all()
        serializer = FeaturesSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        check = Features.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Features.objects.get(pk=kwargs.get('id'))
            serializer = FeaturesSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        check = Features.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Features.objects.get(pk=kwargs.get('id'))
            serializer = FeaturesSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        check = Features.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Features.objects.get(pk=kwargs.get('id'))
            self.perform_destroy(instance)
        else:
            return Response("error: Not found", status=200)
        return Response("success: Destroyed", status=200)


# ---------

# Partners
class PartnersViewSet(ModelViewSet):
    serializer_class = PartnersSerializer
    queryset = Partners.objects.all()
    permission_classes = [ReadOnly]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny | ReadOnly]
        elif self.action in ['list', 'retrieve', 'create', 'update']:
            self.permission_classes = [ReadOnly]
        else:
            self.permission_classes = [ReadOnly]
        return super(PartnersViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = Partners.objects.all()
        serializer = PartnersSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        check = Partners.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Partners.objects.get(pk=kwargs.get('id'))
            serializer = PartnersSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        check = Partners.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Partners.objects.get(pk=kwargs.get('id'))
            serializer = PartnersSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        check = Partners.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Partners.objects.get(pk=kwargs.get('id'))
            self.perform_destroy(instance)
        else:
            return Response("error: Not found", status=200)
        return Response("success: Destroyed", status=200)


# ---------

# News
class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    permission_classes = [ReadOnly]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny | ReadOnly]
        elif self.action in ['list', 'retrieve', 'create', 'update']:
            self.permission_classes = [ReadOnly]
        else:
            self.permission_classes = [ReadOnly]
        return super(NewsViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = News.objects.all()
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        check = News.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = News.objects.get(pk=kwargs.get('id'))
            serializer = NewsSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        check = News.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = News.objects.get(pk=kwargs.get('id'))
            serializer = NewsSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        check = News.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = News.objects.get(pk=kwargs.get('id'))
            self.perform_destroy(instance)
        else:
            return Response("error: Not found", status=200)
        return Response("success: Destroyed", status=200)


# ---------

# AboutService

# class AboutServiceViewSet(ModelViewSet):
#     serializer_class = Serial
#     queryset = Model.objects.all()
#     permission_classes = [ReadOnly]
#
#     def get_permissions(self):
#         if self.action in ['list', 'retrieve']:
#             self.permission_classes = [AllowAny | ReadOnly]
#         elif self.action in ['list', 'retrieve', 'create', 'update']:
#             self.permission_classes = [ReadOnly]
#         else:
#             self.permission_classes = [ReadOnly]
#         return super(View, self).get_permissions()
#
#     def list(self, request, *args, **kwargs):
#         queryset = Modal.objects.all()
#         serializer = Serial(queryset, many=True)
#         return Response(serializer.data, status=200)
#
#     def retrieve(self, request, *args, **kwargs):
#         check = Model.objects.filter(pk=kwargs.get('id'))
#         if check:
#             instance = Model.objects.get(pk=kwargs.get('id'))
#             serializer = Serial(instance, data=request.data, partial=True)
#             serializer.is_valid(raise_exception=True)
#         else:
#             return Response("error: Not found", status=200)
#         return Response(serializer.data)
#
#     def update(self, request, *args, **kwargs):
#         check = Model.objects.filter(pk=kwargs.get('id'))
#         if check:
#             instance = Model.objects.get(pk=kwargs.get('id'))
#             serializer = Serial(instance, data=request.data, partial=True)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#         else:
#             return Response("error: Not found", status=200)
#         return Response(serializer.data, status=200)
#
#     def destroy(self, request, *args, **kwargs):
#         check = Model.objects.filter(pk=kwargs.get('id'))
#         if check:
#             instance = Model.objects.get(pk=kwargs.get('id'))
#             self.perform_destroy(instance)
#         else:
#             return Response("error: Not found", status=200)
#         return Response("success: Destroyed", status=200)


# ---------
