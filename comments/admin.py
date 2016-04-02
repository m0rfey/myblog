import datetime

from django.contrib import admin
from django.contrib.auth.models import User

from comments.models import Comment

class AdminComments(admin.ModelAdmin):
    fields = [
        'comment_user',
        'comment_article',
        #'comment_date',
        'comment_text',
        'comment_like',
    ]
    list_display = ['__str__', 'comment_date']
    list_filter = ['comment_date','comment_user']

admin.site.register(Comment, AdminComments)