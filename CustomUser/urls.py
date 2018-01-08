"""CustomUser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from customization import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', views.home.as_view()),
    url(r'^detail/$',views.detail.as_view()),
    url(r'^countrydetail/([A-Z]+)',views.countrydetail),
    url(r'^$',views.index.as_view()),
    url(r'^signup/$',views.signup.as_view()),
    url(r'^signin/$',views.signin.as_view()),
    url(r'^verifyuser/$',views.VerifyUser.as_view()),
    url(r'^newsignuprequest/$', views.NewSignup.as_view()),
    url(r'^newsigninrequest/$', views.NewSignin.as_view()),
    url(r'^logoutrequest/$',views.Logout.as_view()),
]
