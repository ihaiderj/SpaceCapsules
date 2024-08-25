# ManageCapsuleImages/views.py

from rest_framework import viewsets, serializers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .models import SpaceCapsuleImages, SpaceCapsuleComfortImages, SpaceCapsuleEntertainmentImages
from .serializers import SpaceCapsuleImagesSerializer, SpaceCapsuleComfortImagesSerializer, SpaceCapsuleEntertainmentImagesSerializer

class SpaceCapsuleImagesViewSet(viewsets.ModelViewSet):
    queryset = SpaceCapsuleImages.objects.all()
    serializer_class = SpaceCapsuleImagesSerializer
    parser_classes = (MultiPartParser, FormParser) 

    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError:
            raise serializers.ValidationError({"error": "CapsuleID must be unique."})
        
class SpaceCapsuleComfortImagesViewSet(viewsets.ModelViewSet):
    queryset = SpaceCapsuleComfortImages.objects.all()
    serializer_class = SpaceCapsuleComfortImagesSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError:
            raise serializers.ValidationError({"error": "CapsuleID must be unique."})
        
class SpaceCapsuleEntertainmentImagesViewSet(viewsets.ModelViewSet):
    queryset = SpaceCapsuleEntertainmentImages.objects.all()
    serializer_class = SpaceCapsuleEntertainmentImagesSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError:
            raise serializers.ValidationError({"error": "CapsuleID must be unique."})
