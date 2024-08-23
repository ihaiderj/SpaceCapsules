import os
from django.db import models
from django.utils.text import slugify
from uuid import uuid4

class SpaceCapsuleImages(models.Model):
    CapsuleID = models.CharField(max_length=100, unique=True, primary_key=True)
    modelNumber = models.CharField(max_length=100, null=True)
    brandName = models.CharField(max_length=100, null=True)
    featureType = models.CharField(max_length=100, null=True)    
    mainImage = models.ImageField(upload_to='capsule_images/main/')   

   
  
    def save(self, *args, **kwargs):
        super(SpaceCapsuleImages, self).save(*args, **kwargs)  # First, save the object to ensure the image is uploaded

        # Now, proceed with renaming the image
        self.rename_image(self.mainImage, 'Space-Capsule')

        # Save again to update the image field with the new file name
        super(SpaceCapsuleImages, self).save(update_fields=['mainImage'])

    def rename_image(self, image_field, suffix):
        if image_field and os.path.exists(image_field.path):
            try:
            # Get the current file path
                old_path = image_field.path
                    
            # Generate a new filename
                new_filename = f"{slugify(self.modelNumber)}_{suffix}_{self.brandName}_{self.featureType}_{uuid4().hex}{os.path.splitext(old_path)[1]}"
                new_path = os.path.join(os.path.dirname(old_path), new_filename)

            # Rename the file
                os.rename(old_path, new_path)

            # Update the image field to the new file path
                image_field.name = os.path.join(image_field.field.upload_to, new_filename)
            except FileNotFoundError:
            # Handle the case where the file doesn't exist
                print(f"File {old_path} not found during renaming process.")

    def __str__(self):
        return f"Capsule {self.CapsuleID}"

   
    
class SpaceCapsuleComfortImages(models.Model):
    CapsuleID = models.CharField(max_length=100, unique=True, primary_key=True)
    modelNumber = models.CharField(max_length=100, null=True)
    brandName = models.CharField(max_length=100, null=True)
    featureType = models.CharField(max_length=100, default= 'comfort')    
    airConditioningImage  = models.ImageField(upload_to='capsule_images/comfort/AC/',  null=True)
    heatingImage   = models.ImageField(upload_to='capsule_images/comfort/heating',  null=True)
    freshAirSystemImage    = models.ImageField(upload_to='capsule_images/comfort/freshAirSystem',  null=True)
    floorHeatingImage  = models.ImageField(upload_to='capsule_images/comfort/floorHeatingImage', null=True)
    waterFiltrationSystemImage = models.ImageField(upload_to='capsule_images/comfort/waterFiltrationSystemImage',  null=True)
    privacyBlindsImage     = models.ImageField(upload_to='capsule_images/comfort/privacyBlindsImage',  null=True)
    skylightImage      = models.ImageField(upload_to='capsule_images/comfort/skylightImage',  null=True)
    blockoutBlindsImage     = models.ImageField(upload_to='capsule_images/comfort/blockoutBlindsImage',  null=True)   
    skylightBlindImage     = models.ImageField(upload_to='capsule_images/comfort/skylightBlindImage',  null=True)
    otherComfortImage     = models.ImageField(upload_to='capsule_images/comfort/otherComfortImage',  null=True)
    
 
   
    def save(self, *args, **kwargs):
        super(SpaceCapsuleComfortImages, self).save(*args, **kwargs)  # Save the object first to generate ID if needed

        # Rename images
        self.rename_image(self.airConditioningImage, 'Sapce-Capsule')
        self.rename_image(self.heatingImage, 'Sapce-Capsule')
        self.rename_image(self.freshAirSystemImage, 'Sapce-Capsule')
        self.rename_image(self.floorHeatingImage, 'Sapce-Capsule')
        self.rename_image(self.waterFiltrationSystemImage , 'Sapce-Capsule')
        self.rename_image(self.privacyBlindsImage, 'Sapce-Capsule')
        self.rename_image(self.blockoutBlindsImage, 'Sapce-Capsule')
        self.rename_image(self.skylightImage, 'Sapce-Capsule')
        self.rename_image(self.skylightBlindImage, 'Sapce-Capsule')
        self.rename_image(self.otherComfortImage, 'Sapce-Capsule')
       
        # Save again to update the image field with the new file name
        super(SpaceCapsuleImages, self).save(update_fields=['airConditioningImage', 'heatingImage' ,'freshAirSystemImage',
                    'floorHeatingImage', 'waterFiltrationSystemImage','privacyBlindsImage' ,'blockoutBlindsImage' 
                    ,'skylightImage' ,'skylightBlindImage' ,'otherComfortImage'])
        

    def rename_image(self, image_field, suffix):
        if image_field and os.path.exists(image_field.path):
            try:
            # Get the current file path
                old_path = image_field.path
                    
            # Generate a new filename
                new_filename = f"{slugify(self.modelNumber)}_{suffix}_{self.brandName}_{self.featureType}_{uuid4().hex}{os.path.splitext(old_path)[1]}"
                new_path = os.path.join(os.path.dirname(old_path), new_filename)

            # Rename the file
                os.rename(old_path, new_path)

            # Update the image field to the new file path
                image_field.name = os.path.join(image_field.field.upload_to, new_filename)
            except FileNotFoundError:
            # Handle the case where the file doesn't exist
                print(f"File {old_path} not found during renaming process.")

    def __str__(self):
        return f"Capsule {self.CapsuleID}"