from django.urls import path
from django.conf.urls import url
from .views import *

app_name="lessons"

urlpatterns = [
   
	path('index/', lesson_index, name="index"),
	path('lesson/create', lesson_create, name="create"),
	url(r'^(?P<slug>[\w-]+)/$', lesson_detail, name="detail"),
	url(r'^(?P<slug>[\w-]+)/update/', lesson_update, name="update"),
	url(r'^(?P<slug>[\w-]+)/delete/', lesson_delete, name="delete"),
]