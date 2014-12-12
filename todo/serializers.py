# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='id')

    class Meta:
        model = Todo
        fields = ('id', 'name', 'priority', 'created_by', 'created_at',
                  'is_completed',)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, required=True)
    password = serializers.CharField(max_length=30, required=True,
                                     write_only=True)
    email = serializers.EmailField(required=True)
