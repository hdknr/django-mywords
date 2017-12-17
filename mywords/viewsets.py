from collections import OrderedDict
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, pagination
from rest_framework.response import Response
from . import models, serializers, filters


class Pagination(pagination.PageNumberPagination):
    page_size = 16
    max_page_size = 16
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page_range', list(self.page.paginator.page_range)),
            ('current_page', self.page.number),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class WordViewSet(viewsets.ModelViewSet):

    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializer
    filter_class = filters.WordFilter
    permission_classes = (IsAuthenticated, )
    pagination_class = Pagination


class LinkViewSet(viewsets.ModelViewSet):

    queryset = models.Link.objects.all()
    serializer_class = serializers.LinkSerializer
    filter_class = filters.LinkFilter
    permission_classes = (IsAuthenticated, )
    pagination_class = Pagination
