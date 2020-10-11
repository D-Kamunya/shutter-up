from django.db import models

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
        cls.objects.get(id).delete() 


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
        cls.objects.get(id).delete()             
