from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class POI(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='POIs')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/images/', null=True)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now=True)
    tag = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} 
        {self.title} 
        {self.description} 
        {self.image} 
        {self.date}
        {self.tag}"
    

