from rest_framework import serializers
from core.models import PointOfInterest, TellYourStory

class POISerializer(serializers.ModelSerializer):

    # user = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = PointOfInterest
        fields = [
            #'user',
            'location_name',
            'notes',
            'street_address',
            'city',
            'state',
            'zip_code',
            'images',
            'category',
            'date_created',
            'TellYourStories',
        ]

class TYSSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TellYourStory
        fields = [
            #'user',
            'text',
            'images',
            'date_created',
        ]


# class TellYourStory(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='TellYourStories')    
#     text = models.TextField(max_length=255, null=True, blank=True)
#     image = models.ImageField(upload_to='media/images/', null=True, blank=True)
#     date_created = models.DateField(auto_now=True)
