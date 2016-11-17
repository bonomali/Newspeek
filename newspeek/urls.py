from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import news.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', news.views.index, name='index'),
    url(r'^db', news.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
