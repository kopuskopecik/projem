from django.urls import path
from django.conf.urls import url
from .views import *

app_name="tur"

urlpatterns = [

	path('tr/icerik/', tur_index, name="index"),
	path('tr/create', tur_create, name="create"),
	url(r'^tr/(?P<slug>[\w-]+)/$', tur_detail, name="detail"),
	url(r'^tr/(?P<slug>[\w-]+)/update/', tur_update, name="update"),
	url(r'^tr/(?P<slug>[\w-]+)/delete/', tur_delete, name="delete"),
]