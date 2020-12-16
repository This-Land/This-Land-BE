from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class PointOfInterest(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='Points_of_interest')    
    location_name = models.TextField(max_length=50)
    notes = models.TextField(blank=True)
    street_address = models.CharField(verbose_name='Street Address', max_length=255)
    city = models.CharField(verbose_name='City', max_length=55)
    state = models.CharField(verbose_name='State', max_length=25)
    zip_code = models.CharField(verbose_name='Zip', max_length=5)
    images = models.ImageField(upload_to='media/images/', null=True)
    category = models.CharField(max_length=35)
    date_created = models.DateField(auto_now=True)

    # def __str__(self):
    #     return f'{self.user} {self.comments}'
    
    

    
        

# class Comments(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
#     point_of_interest = models.ForeignKey(to=PointOfInterest, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
#     text = models.TextField(max_length=255, null=True, blank=True)
#     image = models.ImageField(upload_to='media/core_images/', null=True, blank=True
    

