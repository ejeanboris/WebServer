from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='blogIndex'),
    url(r'^refresh/', views.update, name='refresh'),
    ]
