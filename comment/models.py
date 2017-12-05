# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from foodlist.models import Menu

class Comment(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )

    target = models.CharField(max_length=256, verbose_name="评论目标")
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    website = models.URLField(blank=True, verbose_name="网站")
    email = models.EmailField(verbose_name="邮箱")
    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "评论"
        ordering = ['-created_time']
