from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^valida_login/', 'pessoas.views.valida_login'),
    url(r'^$', 'core.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
