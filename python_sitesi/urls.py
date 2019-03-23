"""python_sitesi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from home.views import home_view

from home.sitemaps import DerslerSitemap 
from home.sitemaps import StaticViewSitemap, StaticDerslerViewSitemap


sitemaps = {
	'static' : StaticDerslerViewSitemap,
	'dersler': DerslerSitemap,
	'static' : StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
	path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
	path('', home_view, name="home"),
	path('', include('hakkimizda.urls')),
	path('', include('tur.urls')),
	
	
]
