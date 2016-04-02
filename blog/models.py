#-*- coding: utf-8 -*-
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
import datetime


class Article(models.Model):
    article_title = models.CharField(max_length=200, verbose_name='Заголовок')
    article_text = RichTextUploadingField( verbose_name='Текст') #models.TextField(verbose_name='Текст')
    article_date_add = models.DateTimeField(verbose_name='Дата создания', default=datetime.datetime.now())
    article_date_update =models.DateTimeField(verbose_name='Дата изминения', auto_now=True)
    article_user = models.ForeignKey(User, verbose_name='Пользователь')
    article_likes = models.IntegerField(default=0, verbose_name='Понравилось')
    article_dislikes = models.IntegerField(default=0, verbose_name='Не понравилось')
    article_image = models.ImageField(null=True, blank=True, upload_to="image/", verbose_name='Картинка')
    is_publish = models.IntegerField(default=0, verbose_name='Опубликовать')

    class Meta():
        verbose_name= 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-id']

    def __str__(self):
        return str(self.article_title)

    def bit(self):
        if self.article_image:
            return u'<img src="%s" width="/0"/>'% self.article_image.url
        else:
            return u'Нет изображения'
    bit.short_description = 'Изображение'
    bit.allow_tags = True

    def publish(self):
        if self.is_publish == 1:
            return 'Да'
        else:
            return 'Нет'
    publish.short_description = 'Опубликовано'
    publish.allow_tags = True
