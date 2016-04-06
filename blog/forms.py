# -*- coding: utf-8 -*-
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm
from comments.models import Comment

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class CommentForm(ModelForm):
    #comment_text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Comment
        fields = ['comment_text']



class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
