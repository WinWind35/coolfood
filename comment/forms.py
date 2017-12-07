# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    target = forms.CharField(max_length=256, widget=forms.widgets.HiddenInput)
    nickname = forms.CharField(max_length=50, label='昵称', widget=forms.widgets.HiddenInput)
    email = forms.EmailField(label='邮箱', required=False, widget=forms.widgets.HiddenInput)
    website = forms.CharField(max_length=100, label='网站(选填)', required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'size': '60', 'height': '40', 'class': 'form-control'}),
                              label='评论内容', max_length=1900)
    class Meta:
        model = Comment
        fields = ['target', 'nickname', 'email', 'website',
                  'content']