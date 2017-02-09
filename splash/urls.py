"""Vala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from . import views
#from django.contrib import admin
from views import editEntry
from views import viewEntry
from views import reviewEntry

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^edit/(?P<entry_id>[0-9]+)/$', editEntry.as_view()),
    url(r'^view/(?P<entry_id>[0-9]+)/$', viewEntry.as_view()),
    url(r'^review/(?P<entry_id>[0-9]+)/$', reviewEntry.as_view()),
    url(r'^$', views.splashIndex.as_view()),
]
