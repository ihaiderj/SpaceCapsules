from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpaceCapsuleImagesViewSet, SpaceCapsuleComfortImagesViewSet, SpaceCapsuleEntertainmentImagesViewSet
router = DefaultRouter()
router.register(r'space-capsule-images', SpaceCapsuleImagesViewSet)
router.register(r'space-capsule-comfort-images', SpaceCapsuleComfortImagesViewSet)
router.register(r'space-capsule-comfort-images', SpaceCapsuleEntertainmentImagesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]