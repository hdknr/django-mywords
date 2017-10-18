# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe as _S
from mywords.texts import Markdown
register = template.Library()


@register.filter
def markdown(text):
    return _S(Markdown()(text))
