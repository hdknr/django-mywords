# coding: utf-8

from django.contrib import admin
from ordered_model.admin import OrderedTabularInline
from . import models


class LinkAdminInline(OrderedTabularInline):
    model = models.Link
    extra = 1
    readonly_fields = ['id', 'content_object',  'order', 'move_up_down_links', ]
    raw_id_fields = ['content_type', ]


@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', ]
    inlines = [LinkAdminInline]

    def get_urls(self):
        urls = super(WordAdmin, self).get_urls()
        for inline in self.inlines:
            if hasattr(inline, 'get_urls'):
                urls = inline.get_urls(self) + urls
        return urls
