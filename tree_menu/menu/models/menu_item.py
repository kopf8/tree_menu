from django.db import models
from django.urls import reverse, NoReverseMatch

from menu.models import Menu
from menu.constants import (
    TITLE_MAX_LEN,
    URL_MAX_LEN,
    NAMED_URL_MAX_LEN,
)

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu,
                             on_delete=models.CASCADE,
                             verbose_name='меню',
                             related_name='items',)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               related_name='children',)
    title = models.CharField('заголовок пункта меню',
                             max_length=TITLE_MAX_LEN,)
    url = models.CharField('явный URL',
                           max_length=URL_MAX_LEN,
                           blank=True,
                           help_text='например, /contacts/',)
    named_url = models.CharField('именованный URL',
                                 max_length=NAMED_URL_MAX_LEN,
                                 blank=True,
                                 help_text='например, app:view_name',)
    order = models.PositiveIntegerField('порядок сортировки',
                                        default=0,)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title

    def get_url(self):
        """Используем reverse именованного URL, или используем явный URL."""
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return self.url or ''
        return self.url or ''
