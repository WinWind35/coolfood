# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView
from django.core.cache import cache

from .models import Menu, Category, Tag
from comment.models import Comment
from config.models import SideBar
from comment.forms import CommentForm


class CommonMixin(object):
    def get_context_data(self, **kwargs):
        categories = Category.objects.filter(status=1)

        nav_cates = []
        cates = []
        for cate in categories:
            if cate.is_nav:
                nav_cates.append(cate)
            else:
                cates.append(cate)

        side_bars = SideBar.objects.filter(status=1)

        recently_menus = Menu.objects.filter(status=1)[:10]
        hot_menus = Menu.objects.filter(status=1).order_by('-pv')[:10]
        recently_comments = Comment.objects.filter(status=1)[:10]

        kwargs.update({
            'nav_cates': nav_cates,
            'cates': cates,
            'side_bars': side_bars,
            'recently_menus': recently_menus,
            'hot_menus': hot_menus,
            'recently_comments': recently_comments,
        })
        return super(CommonMixin, self).get_context_data(**kwargs)


class BasePostView(CommonMixin, ListView):
    model = Menu
    template_name = 'foodlist/list.html'
    context_object_name = 'menus'
    paginate_by = 5


class IndexView(BasePostView):
    def get_queryset(self):
        query = self.request.GET.get('query')
        qs = super(IndexView, self).get_queryset()
        if not query:
            return qs

        return qs.filter(name__icontains=query)

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        return super(IndexView, self).get_context_data(query=query)


class CategoryView(BasePostView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id=cate_id)
        return qs


class TagView(BasePostView):
    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []

        menus = Menu.objects.filter(tags=tag)
        return menus


class MenuView(CommonMixin, DetailView):
    model = Menu
    template_name = 'foodlist/detail.html'
    context_object_name = 'menu'

    def get(self, request, *args, **kwargs):
        response = super(MenuView, self).get(request, *args, **kwargs)
        self.pv_uv()
        return response

    def pv_uv(self):
        sessionid = self.request.COOKIES.get('sessionid')
        if not sessionid:
            return

        pv_key = 'pv:%s:%s' % (sessionid, self.request.path)
        if not cache.get(pv_key):
            self.object.increase_pv()
            cache.set(pv_key, 1, 30)

        uv_key = 'uv:%s:%s' % (sessionid, self.request.path)
        if not cache.get(uv_key):
            self.object.increase_uv()
            cache.set(uv_key, 1, 60 * 60 * 24)

    def get_context_data(self, **kwargs):
        comments = Comment.objects.filter(target=self.request.path)
        comment_form = CommentForm(initial={'target': self.request.path})
        kwargs.update({'comments': comments,
                       'comment_form': comment_form,
                       })
        return super(MenuView, self).get_context_data(**kwargs)