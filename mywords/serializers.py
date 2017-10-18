# encoding: utf-8
from rest_framework import serializers
from . import models


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Word
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField()

    class Meta:
        model = models.Link
        fields = '__all__'
