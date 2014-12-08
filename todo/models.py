# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    name = models.CharField(max_length=200)
    priority = models.IntegerField(default=1)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
