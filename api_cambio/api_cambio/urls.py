# -*- coding: utf-8 -*-
# coding: utf-8

"""
URL configuration for api_cambio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views_forex

# from app2 import views as views_app2

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('cambio_forex/', views_forex.convert_currency),
    # path('cambio_awesome/', views_awesome.convert_currency),
]




# urlpatterns = [
#     path('convert/', views.convert_currency),
# ]