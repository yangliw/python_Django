"""meiduo_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
import sys

from django.apps import apps
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

# 测试日志

from meiduo_mall.settings import BASE_DIR


def log(request):
    import logging
    # 拿到的logger配置,创建日志记录器
    logger = logging.getLogger('django')
    logger.error('error')
    return HttpResponse('log')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/',log),
    path('', include('apps.users.urls')),
    path('',include('biao.urls'))
]
