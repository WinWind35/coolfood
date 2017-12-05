# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'password', 'password']
