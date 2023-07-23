from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Clothing(models.Model):
    label = models.CharField(max_length=50, null=False)    
    image = models.ImageField(null=False)    
    type = models.CharField(max_length=20, null=False)
    category = models.CharField(max_length=20, null=False)
    hot =  models.BooleanField(default=True)
    hexcode = models.CharField(max_length=7, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
