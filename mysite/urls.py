from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth import login

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^logins/', include('logins.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'logins.views.login_user'),
    
)


