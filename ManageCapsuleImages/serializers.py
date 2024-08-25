from rest_framework import serializers
from .models import SpaceCapsuleImages, SpaceCapsuleComfortImages, SpaceCapsuleEntertainmentImages

class SpaceCapsuleImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceCapsuleImages
        fields = '__all__'

class SpaceCapsuleComfortImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceCapsuleComfortImages
        fields = '__all__'
        
class SpaceCapsuleEntertainmentImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceCapsuleEntertainmentImages
        fields = '__all__'
