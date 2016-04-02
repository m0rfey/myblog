#-*- coding: utf-8 -*-
import datetime

from django.contrib.auth.models import User
from django.db import models

from blog.models import Article


class Comment(models.Model):
    comment_user = models.ForeignKey(User, verbose_name='Пользователь')
    comment_article = models.ForeignKey(Article, verbose_name='Статья')
    comment_date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    comment_text = models.TextField(verbose_name='Комментарий')
    comment_like = models.IntegerField(default=0, verbose_name='Понравилось')

    class Meta():
        verbose_name = 'Коментарии'
        verbose_name_plural = 'Коментарии'
        ordering=['-comment_date']

    def __str__(self):
        return self.comment_user.username+" / "+self.comment_article.article_title
