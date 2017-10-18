# coding: utf-8
import rest_framework_filters as filters
from . import models


class WordFilter(filters.FilterSet):

    class Meta:
        model = models.Word
        fields = {
            'text':  ['contains', 'exact', 'in', 'startswith'],
        }


class LinkFilter(filters.FilterSet):

    class Meta:
        model = models.Link
        fields = {
            'word__text':  ['contains', 'exact', 'in', 'startswith'],
        }
