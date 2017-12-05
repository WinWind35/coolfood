# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'target', 'status', 'content', 'nickname', 'created_time'
    ]
    list_filter = ['target', 'status']
    search_fields = ['target', 'content', 'nikename']
    save_on_top = True
    show_full_result_count = True

    actions_on_top = True
    date_hierarchy = 'created_time'

    # 编辑页面
    save_on_top = True
    # exclude = ('nickname', 'email',)
    #
    # def save_model(self, request, obj, form, change):
    #     obj.nickname = request.user
    #     obj.email = request.user.email
    #     return super(CommentAdmin, self).save_model(request, obj, form, change)
