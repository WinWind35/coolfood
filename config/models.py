# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from comment.models import Comment


class Link(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    href = models.URLField(verbose_name="链接")  # 默认长度200
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)),
                                         verbose_name="权重",
                                         help_text="权重越高展示顺序约靠前")

    owner = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "友链"


class SideBar(models.Model):
    STATUS_ITEMS = (
        (1, '展示'),
        (2, '下线'),
    )
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新菜肴'),
        (3, '最热菜肴'),
        (4, '最近评论'),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE,
                                               verbose_name="展示类型")
    content = models.CharField(max_length=500, blank=True, verbose_name="内容",
                               help_text="如果设置的不是HTML类型，可为空")

    owner = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "侧边栏"


class UserModel(models.Model):
    SEX_TYPE = (
        (0, '保密'),
        (1, '男'),
        (2, '女'),
    )
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '冻结'),
        (3, '删除'),
    )

    username = models.CharField(blank=True, max_length=64, verbose_name="用户名")
    password = models.CharField(max_length=16, verbose_name="密码")
    created_time = models.DateField(auto_now_add=True, verbose_name="注册时间")

    email = models.EmailField(verbose_name="邮箱")
    birth = models.DateField(auto_now_add=True, verbose_name="生日")
    sex = models.IntegerField(choices=SEX_TYPE, default=0, verbose_name="性别")
    question = models.CharField(max_length=256, null=True, verbose_name="密保问题")
    answer = models.CharField(max_length=256, null=True, verbose_name="密保答案")

    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name="用户状态")

    class Meta:
        verbose_name = verbose_name_plural = "用户系统"
