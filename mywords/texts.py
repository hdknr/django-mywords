import copy
import re
from mistune import (
    Renderer, InlineGrammar, InlineLexer,
    Markdown as BaseMarkdown,
)
from .models import Link


class WikiLinkRenderer(Renderer):
    def wiki_link(self, alt, link):
        return '<a href="%s">%s</a>' % (link, alt)

class WikiLinkInlineLexer(InlineLexer):
    def enable_wiki_link(self):
        # add wiki_link rules
        self.rules.wiki_link = re.compile(
            r'\[\['                   # [[
            r'([\s\S]+?)'   # Page 2|Page 2
            r'\]\](?!\])'             # ]]
        )

        # Add wiki_link parser to default rules
        # you can insert it some place you like
        # but place matters, maybe 3 is not good
        self.default_rules.insert(3, 'wiki_link')

    def output_wiki_link(self, m):
        text = m.group(1)
        link = Link.objects.filter(word__text=text).first()
        if link:
            return self.renderer.wiki_link(link.text, link.url)
        return text


class Markdown(BaseMarkdown):

    def __init__(self, renderer=None, inline=None, block=None, **kwargs):
        if not inline:
            renderer = WikiLinkRenderer()
            inline = WikiLinkInlineLexer(renderer)
            inline.enable_wiki_link()

        super(Markdown, self).__init__(
            renderer=renderer, inline=inline, block=block, **kwargs)
