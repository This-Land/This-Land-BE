from rest_framework import serializers
from core.models import PointOfInterest

class POISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PointOfInterest
        fields = [
            'location_name',
            'notes',
            'street_address',
            'city',
            'state',
            'zip_code',
        ]

    # user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='PointsOfInterest')    
    # location_name = models.TextField(max_length=50)
    # comments = models.TextField(blank=True)
    # street_address = models.CharField(verbose_name='Street Address', max_length=255)
    # city = models.CharField(verbose_name='City', max_length=55)
    # state = models.CharField(verbose_name='State', max_length=25)
    # zip_code = models.CharField(verbose_name='Zip', max_length=5)
    # images = models.ImageField(upload_to='media/images/', null=True)
    # category = models.CharField(max_length=35)
    # date_created = models.DateField(auto_now=True)