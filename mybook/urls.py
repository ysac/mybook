from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mybook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cms/', include('cms.urls', namespace='cms')),   # ←ここを追加
    url(r'^api/', include('api.urls', namespace='api')),  # ここを追加
)