# coding:utf-8
from __future__ import unicode_literals

from dal import autocomplete
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Tag


class MenuAdminForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=autocomplete.ModelSelect2(url='category-autocomplete'),
        label='分类',
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        label='标签',
    )
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='正文', required=True)
