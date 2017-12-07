# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView,TemplateView
from django.contrib.auth.forms import UserCreationForm

from comment.forms import CommentForm
from comment.models import Comment
from foodlist.views import CommonMixin
from .forms import UserForm
from .models import Link


class LinkView(CommonMixin, ListView):
    model = Link
    template_name = 'config/links.html'
    context_object_name = 'links'

    def get_queryset(self):
        query = Link.objects.filter(status=1)
        return query

    def get_context_data(self, **kwargs):
        comments = Comment.objects.filter(target='/links/')
        kwargs.update({
            'comment_form': CommentForm(),
            'comments': comments,
        })
        return super(LinkView, self).get_context_data(**kwargs)


class RegisterView(TemplateView):
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        register_form = UserCreationForm()
        context = {
            'register_form': register_form,
            'next': request.GET.get('next')
        }
        return self.render_to_response(context)
        # return super(RegisterView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            succeed = True
        else:
            succeed = False

        context = {
            'succeed': succeed,
            'register_form': register_form,
        }
        return self.render_to_response(context)