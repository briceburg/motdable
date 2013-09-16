from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register(r'playcalls', views.PlayCallViewSet)
router.register(r'playcalloptions', views.PlayCallOptionViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls))
)

urlpatterns += patterns('',
    url(r'^auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)