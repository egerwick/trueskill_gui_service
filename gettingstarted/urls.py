from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
import hello.views

router = routers.DefaultRouter()
router.register(r'groups', hello.views.GameViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^games/$', hello.views.GameList.as_view()),
    url(r'^games/(?P<pk>[0-9]+)/$', hello.views.GameDetail.as_view()),
]
