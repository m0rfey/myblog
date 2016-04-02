from django.forms import ModelForm
from django import forms

from comments.models import Comment


class CommentForm(ModelForm):
    comment_text = forms.CharField(
        label='',
        max_length=300,
        widget = forms.Textarea({'class': 'form-control','rows':'5', 'placeholder': 'Комментврий...'})
    )

    class Meta:
        model = Comment
        fields = ['comment_text']

'''
    def save(self, comment_user, comment_article):
        obj = super(CommentForm, self).save(commit=False)
        obj.user = comment_user
        obj.article = str(comment_article)
        return obj.save
'''