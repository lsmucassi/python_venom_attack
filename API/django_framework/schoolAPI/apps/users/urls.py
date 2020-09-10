from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlspatterns = [
    path('', include(router.urls)),
]

