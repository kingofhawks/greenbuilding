from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'greenbuilding.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^core/', include('core.urls')),
    url(r'^enterprise/', include('enterprise.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
