from django.conf.urls import patterns, include
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

handler500 = 'lfs.core.views.server_error'

urlpatterns = patterns("",
    (r'', include('lfs.core.urls')),
    (r'^manage/', include('lfs.manage.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^paypal/ipn/', include('paypal.standard.ipn.urls')),
    (r'^reviews/', include('reviews.urls')),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

try:
    from local_urls import *
except ImportError:
    pass
