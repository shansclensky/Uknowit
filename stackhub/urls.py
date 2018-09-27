from django.conf.urls import url
from django.contrib.auth.views import login

from stackhub.views import(
    logout_page,
    my_view,
    post_questionpage,
    question_detailpage,
    profile_page,
    home,
    search,
    answer_update,

)

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^logout/$', logout_page,name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^my_view/$',my_view,name='my_view'),
    url(r'^post_questionpage/$',post_questionpage,name='post_questionpage'),
    url(r'^question_detailpage/(?P<q_id>[0-9]+)/$', question_detailpage, name='question_detailpage'),
    url(r'^profile_page/$',profile_page,name='profile_page'),
    url(r'^search/$', search, name='search'),
    url(r'^answer_update/$',answer_update,name='answer_update'),

]
