from django.contrib.contenttypes.models import ContentType


class Word(object):

    def add_link(self, instance):
        return self.link_set.get_or_create(
            content_type=ContentType.objects.get_for_model(instance),
            object_id=instance.id)
