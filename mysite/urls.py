from django.conf.urls import patterns, include, url
#from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    #url(r'^index/', TemplateView.as_view(template_name="layout.html")),
)


#urlpatterns += patterns('django.contrib.flatpages.views',
#                        url(r'^about-us/$', 'flatpage', {'url': '/about-us/'}, name='about'),
#                        url(r'^license/$', 'flatpage', {'url': '/license/'}, name='license'),
#                        )
