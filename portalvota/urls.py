from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.index'),
    url(r'^votacao/$', 'core.views.votacao'),
    url(r'^obrigado/$', 'core.views.obrigado'),
    url(r'^vencedores/$', 'core.views.vencedores'),
    url(r'^admin/', include(admin.site.urls)),
)
