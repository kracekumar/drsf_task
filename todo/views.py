# -*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework import filters

from .models import Todo, User
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_fields = ('priority', 'created_by', 'is_completed')
    filter_backends = [filters.OrderingFilter]
