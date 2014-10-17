from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from random import randint
import time
import models


class CssBackgroundPlugIn(CMSPluginBase):
    model = models.CssBackground
    name = 'CSS Background'
    render_template = 'css_background.html'
    raw_id_fields = ('image',)
    fieldsets = (
        (None, {
            'fields': ('bg_type', 'image', ('r', 'g', 'b', 'a')),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'time': '-'.join([
                str(instance.id),
                str(randint(0, 100000) if not instance.image else instance.image.id),
                repr(time.time()).replace('.', '_')]),
        })
        return context

plugin_pool.register_plugin(CssBackgroundPlugIn)
