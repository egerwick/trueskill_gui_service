from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^db', hello.views.db, name='db'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^games/$', hello.views.GameList.as_view()),
    url(r'^players/$', hello.views.PlayerList.as_view()),
    url(r'^ratings/$', hello.views.RatingList.as_view())
]