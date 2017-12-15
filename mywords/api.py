# coding: utf-8
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register(r'word', viewsets.WordViewSet, base_name='word')
router.register(r'link', viewsets.LinkViewSet, base_name='link')

urlpatterns = [
    url(r'^', include(router.urls)),
]
