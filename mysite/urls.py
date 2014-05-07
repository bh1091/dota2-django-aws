from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),    
    url(r'^search/$', 'search.views.search'),
    url(r'^banpick/$', 'banpick.views.banpick'),
    url(r'^news/$', 'news.views.news'),
    url(r'^live/$','live.views.present_live'),
    url(r'^live/(.+)/$','live.views.watch'),
)
