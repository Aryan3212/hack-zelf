from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from hack_aggregator import views

router = routers.DefaultRouter()
router.register(r'contents', views.ListContentView, basename='content-list')
urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
