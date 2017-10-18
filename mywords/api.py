# coding: utf-8
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'words', views.WordViewSet, base_name='word')
router.register(r'links', views.LinkViewSet, base_name='link')

urlpatterns = [
    url(r'^api/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
