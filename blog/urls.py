from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
	url('',views.post_list, name='post_list'),
]