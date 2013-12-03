from django.conf.urls import patterns, url

from logins import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<department_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/

)