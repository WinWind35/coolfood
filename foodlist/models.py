# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import F

from django.contrib.auth.models import User
from django.db import models


class Menu(models.Model):
    STATUS_ITEMS = (
        (1, '上线'),
        (2, '草稿'),
        (3, '删除'),
    )
    name = models.CharField(max_length=64, verbose_name='菜名')
    ingredients = models.CharField(max_length=128, verbose_name='食材')
    category = models.ForeignKey('Category', max_length=64, verbose_name='分类')
    tags = models.ManyToManyField('Tag', related_name="menus", verbose_name="标签")
    content = models.TextField(verbose_name="内容", blank=True,  help_text="注：目前仅支持Markdown格式数据")
    status = models.IntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, verbose_name="作者")

    pv = models.PositiveIntegerField(default=0)
    uv = models.PositiveIntegerField(default=0)

    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def status_show(self):
        return '当前状态:%s' % self.status
    status_show.short_description = '展示状态'

    def __unicode__(self):
        return self.name

    def increase_pv(self):
        return type(self).objects.filter(pk=self.pk).update(pv=F('pv') + 1)

    def increase_uv(self):
        return type(self).objects.filter(pk=self.pk).update(uv=F('uv') + 1)

    class Meta:
        verbose_name = verbose_name_plural = "菜肴"
        ordering = ['-created_time']


class Category(models.Model):
    STATUS_ITEMS = (
        (1, '可用'),
        (2, '删除'),
    )
    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")

    owner = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )

    name = models.CharField(max_length=10, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")

    owner = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '标签'
