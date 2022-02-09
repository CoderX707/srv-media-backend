from django.db import models
from user_auth_api.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Channel(models.Model):
    channel_title = models.CharField(max_length=40)
    channel_description = models.TextField()
    channel_image = models.ImageField(default="not_found.jpg")
    subscription_price = models.DecimalField(max_digits=10, decimal_places=2)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='channels')

    def __str__(self):
        return self.channel_title

class Subcription(models.Model):
    subcription_status= models.BooleanField(default=True)
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    days = models.CharField(max_length=40)
    total = models.CharField(max_length=100)

    def __str__(self):
        return self.days

