from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import os
DIRNAME = os.path.dirname(__file__)

urlpatterns = patterns("",
    (r'', include('lfs.core.urls')),
    (r'^manage/', include('lfs.manage.urls')),
)

urlpatterns += patterns("",
    (r'', include('lfs_rest.urls')),
    (r'^reviews/', include('reviews.urls')),
    (r'^paypal/ipn/', include('paypal.standard.ipn.urls')),
    (r'^paypal/pdt/', include('paypal.standard.pdt.urls')),
)

urlpatterns += patterns("",
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(DIRNAME, "media"), 'show_indexes': True }),
)

if hasattr(settings, 'TESTING'):
    if settings.TESTING:
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(DIRNAME, "sitestatic"), 'show_indexes': True }),



urlpatterns += staticfiles_urlpatterns()
