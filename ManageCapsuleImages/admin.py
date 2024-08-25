from django.contrib import admin
from .models import SpaceCapsuleImages, SpaceCapsuleComfortImages, SpaceCapsuleEntertainmentImages

@admin.register(SpaceCapsuleImages)
class SpaceCapsuleImagesAdmin(admin.ModelAdmin):
    list_display = ('CapsuleID', 'modelNumber' , 'brandName', 'mainImage')

@admin.register(SpaceCapsuleComfortImages)
class SpaceCapsuleComfortImagesAdmin(admin.ModelAdmin):
    list_display = ('CapsuleID', 'modelNumber' , 'brandName','airConditioningImage', 'heatingImage' ,'freshAirSystemImage',
                    'floorHeatingImage', 'waterFiltrationSystemImage','privacyBlindsImage' ,'blockoutBlindsImage' 
                    ,'skylightImage' ,'skylightBlindImage' ,'otherComfortImage' )
    

@admin.register(SpaceCapsuleEntertainmentImages)
class SpaceCapsuleEntertainmentImagesAdmin(admin.ModelAdmin):
    list_display = ('CapsuleID', 'modelNumber' , 'brandName','projectImage', 'projectorScreenImage' ,'intelligentControlPanelImage',
                    'integratedSoundSystemImage', 'otherEntertainmentImage')