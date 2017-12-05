# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Menu, Category, Tag
from .forms import MenuAdminForm


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    form = MenuAdminForm
    # 展示页
    list_display = [
        'name', 'category', 'status', 'pv', 'uv', 'created_time'
    ]
    list_filter = ['status', 'category',]
    search_fields = ['name', 'category', 'tags']
    # 编辑页
    # filter_horizontal = ('tags', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
