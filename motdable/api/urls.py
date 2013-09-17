from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register(r'playbooks', views.PlaybookViewSet)
router.register(r'playbookvars', views.PlaybookVariableViewSet)
router.register(r'hosts', views.HostViewSet)
router.register(r'hostcredentials', views.HostCredentialViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls))
)

urlpatterns += patterns('',
    url(r'^auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)