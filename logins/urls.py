from django.conf.urls import patterns, url
from django.views.generic import UpdateView
from logins.views import InfoEdit

from logins import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<info_id>\d+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create, name='create'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^register_success/$', views.register_success, name='register_success'),
    url(r'^(?P<info_id>\d+)/delete/$', views.delete_info, name = 'delete'),
    url(r'^(?P<pk>\d+)/edit/$', InfoEdit.as_view(success_url="/logins/"), name='edit'),
    url(r'^search/$', views.search_infos, name = 'search'),
)
