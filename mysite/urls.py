from django.conf.urls import patterns, include, url
from logins.views import login

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^logins/', include('logins.urls', namespace = "logins")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login, name='default'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls'))
    
)

