from django.db import models
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField


class CssBackground(CMSPlugin):

    BG_CHOICES = (
        ('image', 'image'),
        ('rgb', 'rgb'),
        ('rgba', 'rgba'),
    )

    bg_type = models.CharField(
        max_length=5, choices=BG_CHOICES, default='image')
    image = FilerImageField(
        null=True, blank=True,
        default=None, verbose_name='image')
    r = models.IntegerField(default=0)
    g = models.IntegerField(default=0)
    b = models.IntegerField(default=0)
    a = models.IntegerField(default=0)

    class Meta:
        verbose_name = "css background"

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.bg_type == 'image' and not self.image:
            raise ValidationError('You must select an image')

    @property
    def css_background(self):

        if self.bg_type == 'image':

            return ''.join([
                'background-image: url(',
                self.image.url,
                ');'])

        elif self.bg_type == 'rgb':

            return ''.join([
                'background-color: rgb(',
                str(self.r), ',',
                str(self.g), ',',
                str(self.b), ');'])

        elif self.bg_type == 'rgba':

            return ''.join([
                'background-color: rgba(',
                str(self.r), ',',
                str(self.g), ',',
                str(self.b), ',',
                str(self.a), ');'])

        return ''

    def __unicode__(self):
        if self.bg_type == 'image':
            return self.image.label
        elif self.bg_type == 'rgb':
            return u'rgb: %s-%s-%s' % (self.r, self.g, self.b)
        elif self.bg_type == 'rgba':
            return u'rgba: %s-%s-%s-%s' % (self.r, self.g, self.b, self.a)
