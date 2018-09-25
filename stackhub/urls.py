from django.config.urls import url

from .import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
