from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import SafeString as _S
from django.template import Context, Template


class Word(object):

    def add_link(self, instance):
        return self.link_set.get_or_create(
            content_type=ContentType.objects.get_for_model(instance),
            object_id=instance.id)


class Link(object):

    @property
    def object_admin_url(self):
        name = 'admin:{0}_{1}_change'.format(*self.content_type.natural_key())
        ctx = Context(dict(name=name, id=self.object_id,
                       instance=self.content_object))
        t = '''<a href="{% url name id %}">{{ instance }}</a> '''
        return _S(Template(t).render(ctx))
