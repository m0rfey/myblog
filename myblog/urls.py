"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

import blog.views
import comments.views
import loginsys.views

from myblog import settings

urlpatterns =[
    url(r'^$', blog.views.home, name='home'),
    #url(r'^article-after/(?P<article_id>\d+)/$', blog.views.ajax, name='home_ajax'),
    url(r'^about/$', blog.views.about, name='about'),
    url(r'^article/(?P<article_id>\d+)/$', blog.views.show_article, name='article'),
    url(r'^article/addlike/(?P<article_id>\d+)/$', blog.views.add_like, name='add_like'),
    url(r'^article/adddislike/(?P<article_id>\d+)/$', blog.views.add_dislike, name='add_dislike'),
    url(r'^article/addcomment/(?P<article_id>\d+)/$',  blog.views.add_comment,name='add_comment'),
    url(r'^article/addlikecomm/(?P<comment_id>\d+)/$', comments.views.add_likecomm, name='add_likecomm'),
    url(r'^login/$', loginsys.views.login, name='login'),
    url(r'^logout/$', loginsys.views.logout, name='logout'),
    url(r'^register/$', loginsys.views.register, name='register'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),


    url(r'^admin/', include(admin.site.urls)),
                      ]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
