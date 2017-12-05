"""coolfood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from .autocomplete import CategoryAutocomplete, TagAutocomplete
import ckeditor_uploader
from django.conf.urls import include

from foodlist.views import IndexView, CategoryView, TagView, MenuView
from comment.views import CommentView
from config.views import LinkView, RegisterView

urlpatterns = [
                  url(r'^$', IndexView.as_view(), name="index"),
                  url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name="category"),
                  url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name="tag"),
                  url(r'^menu/(?P<pk>\d+)/$', MenuView.as_view(), name="detail"),
                  url(r'^comment/$', CommentView.as_view(), name="comment"),
                  url(r'^links/$', LinkView.as_view(), name="links"),

                  url(r'^register/$', RegisterView.as_view(), name="register"),
                  url(r'^login/$', LinkView.as_view(), name="links"),

                  url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
                  url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),

                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),

                  url(r'^admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
