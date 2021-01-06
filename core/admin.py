from django.contrib import admin
from .models import PointOfInterest, TellYourStory, User

# Register your models here.

admin.site.register(PointOfInterest)
admin.site.register(TellYourStory)

admin.site.register(User)