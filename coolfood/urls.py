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
from django.conf.urls import include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from django.contrib.auth.views import LoginView, LogoutView

from foodlist.views import IndexView, CategoryView, TagView, MenuView, FavoriteView
from comment.views import CommentView
from config.views import LinkView, RegisterView
from foodlist.api import MenuViewSet, CategoryViewSet, TagViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'tag', TagViewSet)
router.register(r'user', UserViewSet)


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name="category"),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name="tag"),
    url(r'^menu/(?P<pk>\d+)/$', MenuView.as_view(), name="detail"),
    url(r'^favorite/$', FavoriteView.as_view(), name="favorite"),
    url(r'^comment/$', CommentView.as_view(), name="comment"),
    url(r'^links/$', LinkView.as_view(), name="links"),

    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),

    url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^api/docs/', include_docs_urls(title='CoolFood API')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
