from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = CloudinaryField('image')
    description = models.CharField(max_length=400,default=False)
    author = models.CharField(default='Author name..',max_length=100)
    year_published = models.IntegerField(blank=True, null=True)
   
   
    def __str__(self):
      return self.name

    @property
    def save_image(self):
          self.save()

    def delete_image(self):
        self.delete()