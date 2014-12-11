# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from todo.views import TodoViewSet

admin.autodiscover()

router = routers.DefaultRouter()
router.register('todos', TodoViewSet, 'todo')


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drsf_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
