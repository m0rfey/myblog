from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect

from comments.models import Comment
from comments.forms import CommentForm
import datetime

def add_likecomm(request, comment_id):
    try:
        if comment_id in request.COOKIES:
            return_path = request.META.get('HTTP_REFERER', '/')
            return redirect(return_path)
        else:
            comment = Comment.objects.get(id = comment_id)
            comment.comment_like += 1
            comment.save()
            return_path = request.META.get('HTTP_REFERER', '/')
            response = redirect(return_path)
            response.set_cookie(comment_id, 'likecomment')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')