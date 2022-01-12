"""anonproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from anonapp import views
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap

from .sitemaps import PostSitemap

sitemaps = {'post': PostSitemap}

urlpatterns = [
    path('site_map.xml/', sitemap, {'sitemaps': sitemaps}),
    # path('', views.index, name="index"),
    path('post/', views.post, name="post"),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('adminnnnn/', admin.site.urls),
    path('', views.FirstView.as_view(), name="index"),
    path('wizkid/', views.WizView.as_view(), name="wizkid"),
    path('cardb/', views.CardView.as_view(), name="card"),
    path('drake/', views.DrakeView.as_view(), name="drake"),
    path('justin/', views.JustView.as_view(), name="just"),
    path('policy/', views.policy , name="policy"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
