from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpaceCapsuleImagesViewSet, SpaceCapsuleComfortImagesViewSet
router = DefaultRouter()
router.register(r'space-capsule-images', SpaceCapsuleImagesViewSet)
router.register(r'space-capsule-comfort-images', SpaceCapsuleComfortImagesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]