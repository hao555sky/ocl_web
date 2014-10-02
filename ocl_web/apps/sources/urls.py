from django.conf.urls import patterns, url, include
from .views import SourceDetailView, SourceCreateView

__author__ = 'briandant'

urlpatterns = patterns('',
    url(r'^detail/(?P<org>[a-zA-Z0-9\-\.]+)/(?P<source>[a-zA-Z0-9\-\.]+)/$', SourceDetailView.as_view(), name='source-detail'),
    url(r'^create/(?P<org>[a-zA-Z0-9\-\.]+)/$', SourceCreateView.as_view(), name='source-create-for-org'),

#    url(r'^$', SourceListView.as_view(), name='source-list'),
#    url(r'^(?P<source>[a-zA-Z0-9\-\.]+)/versions/$', SourceVersionListView.as_view(), name='sourceversion-list'),
#    url(r'^(?P<source>[a-zA-Z0-9\-\.]+)/latest/$', SourceVersionRetrieveUpdateView.as_view(), {'is_latest': True}, name='sourceversion-latest-detail'),
#    url(r'^(?P<source>[a-zA-Z0-9\-\.]+)/(?P<version>[a-zA-Z0-9\-\.]+)/$', SourceVersionRetrieveUpdateDestroyView.as_view(), name='sourceversion-detail'),
#    url(r'^(?P<source>[a-zA-Z0-9\-\.]+)/(?P<version>[a-zA-Z0-9\-\.]+)/children/$', SourceVersionChildListView.as_view(), {'list_children': True}, name='sourceversion-child-list'),
#    url(r'^(?P<source>[a-zA-Z0-9\-\.]+)/(?P<version>[a-zA-Z0-9\-\.]+)/concepts/', include('apps.concepts.urls'))
)
