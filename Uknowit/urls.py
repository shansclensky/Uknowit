from django.conf.urls import url,include
from django.contrib import admin

app_name = 'stackhub'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('stackhub.urls')),
]
