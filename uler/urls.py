from django.urls import path,include
from django.conf.urls import url
from . import views

app_name='uler'
urlpatterns = [
    url(r'^api/short/$',views.shorter),
    url(r'^api/delete/$',views.dels),
    path('<str:url>', views.index),
]
