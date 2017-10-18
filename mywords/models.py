# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from ordered_model.models import OrderedModel


class Word(models.Model):
    text = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = _('Word')
        verbose_name_plural = _('Words')

    def __str__(self):
        return self.text


class Link(OrderedModel):
    word = models.ForeignKey(Word)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    order_with_respect_to = 'word'
    order_class_path = 'mywords.models.Link'

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')
        ordering = ['word', 'order', ]
