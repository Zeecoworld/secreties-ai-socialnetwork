from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from anonapp import views
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap

from .sitemap import PostSitemap,StaticSiteMap

sitemaps = {'post':PostSitemap,'static':StaticSiteMap}

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
