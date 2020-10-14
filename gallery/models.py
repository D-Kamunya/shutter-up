from django.db import models
import datetime as dt
import pyperclip
from pyuploadcare.dj.models import ImageField
# Create your models here.

class Location(models.Model):
    """
    Location where the photo is taken e.g Nairobi,Kenya
    """

    city = models.CharField(max_length =100)
    country = models.CharField(max_length =100)
    def __str__(self):
      return self.city

    def save_location(self):
        '''
        Saves location instance to db
        '''
        self.save()

    @classmethod
    def del_location(cls,id):
        '''
        Deletes location instance from db
        '''
        cls.objects.get(pk =id).delete() 


class Category(models.Model):
    """
    Category under which the photo taken falls in e.g. Travel,Music,Food
    """
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name 

    def save_category(self):
        '''
        Saves category instance to db
        '''
        self.save()

    @classmethod
    def del_category(cls,id):
        '''
        Deletes category instance from db
        '''
        cls.objects.get(pk =id).delete()    




class Image(models.Model):
    """
    Image class to define Image Objects
    """
    image_name = models.CharField(max_length =150)
    image_path = ImageField(blank=True, manual_crop="")
    image_description = models.CharField(max_length =255)
    location = models.ForeignKey(Location,
    on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name 


    class Meta:
        ordering = ['upload_date'] 

    def save_image(self):
      '''
      Saves image instance to db
      '''
      self.save()


    @classmethod
    def get_all_images(cls):
      '''
      Returns all image objects from db
      '''
      images=cls.objects.all()
      return images 


    @classmethod
    def get_image_by_id(cls,id):
      '''
      Returns image based on its id
      '''
      image=cls.objects.get(id=id)
      return image



    @classmethod
    def delete_image(cls,id):
      '''
      Deletes image based on its id
      '''
      cls.objects.filter(id=id).delete()
      

    @classmethod
    def search_image(cls,category_name):
      '''
      Allows us to search for an image using its category.
      '''
      images=cls.objects.filter(category__name__icontains=category_name)
      return images



    @classmethod
    def filter_by_location(cls,location_id):
      """
      Allows us to filter images by the location.
      """
      images=cls.objects.filter(location__id=location_id)
      return images

    @classmethod
    def copy_image_url(cls,image_id):
      '''
      method that copies image url
      '''
      img_url=cls.objects.get(id=image_id).image_path.url
      pyperclip.copy(img_url)    




 
