from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.index'),
    url(r'^valida_login/$', 'pessoas.views.valida_login'),
    url(r'^votacao/$', 'pessoas.views.votacao'),
    url(r'^voto/(?P<codigo>\d+)/$','pessoas.views.votar'),
    url(r'^obrigado/$', 'core.views.obrigado'),
    url(r'^vencedores/$', 'core.views.vencedores'),
    url(r'^premios/$', 'core.views.premios'),
    url(r'^admin/', include(admin.site.urls)),
)
