from rest_framework import serializers
<<<<<<< HEAD
from core.models import PointOfInterest, TellYourStory, User



class UserSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'id',
        ]
=======
from core.models import PointOfInterest, TellYourStory
>>>>>>> 934c3d3586e63c1c0abb83fa4db306a89eb54785


class TYSSerializer(serializers.ModelSerializer):
    #user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    class Meta:
        model = TellYourStory
        fields = [
            'username',
            'user',
            'username',
            'id',
            'text',
            'images',
            'date_created',
            'poi',
        ]

class POISerializer(serializers.ModelSerializer):
    TellYourStories = TYSSerializer(many=True, read_only=True)
    #user = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = PointOfInterest
        fields = [
            'username',
            'user',
            'username',
            'id',
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