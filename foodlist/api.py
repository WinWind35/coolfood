# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from .models import Menu, Category, Tag


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    created_time = serializers.DateTimeField(format="%Y-%M-%D %H:%M:%S")

    class Meta:
        model = Menu
        fields =(
            'url', 'name', 'ingredients',
            'category', 'tags', 'owner',
            'pv', 'created_time',
        )


class MenuDetailSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    created_time = serializers.DateTimeField(format="%Y-%M-%D %H:%M:%S")

    class Meta:
        model = Menu
        fields =(
            'name', 'ingredients',
            'category', 'tags', 'owner',
            'pv', 'created_time',
            'content',
        )


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(status=1)
    serializer_class = MenuSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = MenuDetailSerializer
        return super(MenuViewSet, self).retrieve(request, *args, **kwargs)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields =(
            'url', 'id', 'name', 'created_time',
        )


class CategoryDetailSerializer(serializers.ModelSerializer):
    menu_set = MenuSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'created_time', 'menu_set',
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=1)
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super(CategoryViewSet, self).retrieve(request, *args, **kwargs)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields =(
            'url', 'id', 'name', 'created_time',
        )


class TagDetailSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Tag
        fields =(
            'id', 'name', 'created_time', 'menus',
        )


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.filter(status=1)
    serializer_class = TagSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = TagDetailSerializer
        import pdb;pdb.set_trace()
        return super(TagViewSet, self).retrieve(request, *args, **kwargs)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =(
            'url', 'id', 'username',
        )


class UserDetailSerializer(serializers.ModelSerializer):
    menu_set = MenuSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = User
        fields =(
            'id', 'username', 'menu_set',
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = UserDetailSerializer
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)