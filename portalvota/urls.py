from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portalvota.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

<<<<<<< HEAD
=======
    url(r'^$', 'core.views.index'),
    url(r'^login/$', 'core.views.login'),
>>>>>>> 58538a7a4c49ccd17961090fc5a71c460815bcce
    url(r'^admin/', include(admin.site.urls)),
)
