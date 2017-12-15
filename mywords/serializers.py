from rest_framework import serializers
from . import models


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Word
        fields = '__all__'

    def is_valid(self, *args, **kwargs):
        res = super(WordSerializer, self).is_valid(*args, **kwargs)
        if not res:
            self._existing_instance = self.Meta.model.objects.filter(
                    text=self.initial_data.get('text', '')).first()
            res = self._existing_instance and True or False
        return res

    def save(self, **kwargs):
        if hasattr(self, '_existing_instance'):
            self.instance = self._existing_instance
            return self.instance
        return super(WordSerializer, self).save(**kwargs)


class LinkSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField()
    text = serializers.ReadOnlyField()

    class Meta:
        model = models.Link
        fields = '__all__'
