# coding:utf-8
from __future__ import unicode_literals

from dal import autocomplete

from foodlist.models import Category, Tag


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Category.objects.filter(status=1)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Tag.objects.filter(status=1)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs