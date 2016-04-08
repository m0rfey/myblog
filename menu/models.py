from django.utils.translation import ugettext_lazy as _
from django.db import models


class Menu(models.Model):
    name = models.CharField(
        _(u'Название'),
        max_length=100
        )

    slug = models.SlugField(
        _(u'Код')
        )

    base_url = models.CharField(
        _(u'Базовый URL'),
        max_length=100,
        blank=True,
        null=True
        )

    description = models.TextField(
        _(u'Описание'),
        blank=True,
        null=True
        )

    class Meta:
        verbose_name = _(u'меню')
        verbose_name_plural = _(u'меню')

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return  str(self.name)

    def save(self, *args, **kwargs):
        """
        Re-order all items from 10 upwards, at intervals of 10.
        This makes it easy to insert new items in the middle of
        existing items without having to manually shuffle
        them all around.
        """
        super(Menu, self).save(*args, **kwargs)

        current = 10
        for item in MenuItem.objects.filter(menu=self).order_by('order'):
            item.order = current
            item.save()
            current += 10


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        verbose_name=_(u'Название')
        )

    order = models.IntegerField(
        _(u'Сортировка'),
        default=500
        )

    link_url = models.CharField(
        _(u'URL'),
        max_length=100,
        help_text=_(u'URL или URI страницы, например /about/ or http://foo.com/')
        )

    title = models.CharField(
        _(u'Заголовок'),
        max_length=100
        )

    login_required = models.BooleanField(
        _(u'Для авторизированных'),
        blank=True,
        help_text=_(u'Если установить, то пункт меню будет показан только для авторизированных пользователей')
        )

    anonymous_only = models.BooleanField(
        _(u'Для анонимных'),
        blank=True,
        help_text=_(u'Если установить, то пункт меню будет показан только для не авторизированных пользователей')
        )

    class Meta:
        verbose_name = _(u'пункт меню')
        verbose_name_plural = _(u'пункты меню')

    def __unicode__(self):
        return u"%s %s. %s" % (self.menu.slug, self.order, self.title)

    def __str__(self):
        return str(self.name)
