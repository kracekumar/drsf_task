# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import TodoSerializer, UserSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_fields = ('priority', 'created_by', 'is_completed')
    filter_backends = [filters.OrderingFilter, filters.DjangoFilterBackend]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class UserListApiView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(data=users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            # check if exists, we ll skip
            # Create User object
            User.objects.create_user(**serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailApiView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
