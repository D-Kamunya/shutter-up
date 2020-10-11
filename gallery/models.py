from django.db import models

# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length =100)
    country = models.CharField(max_length =100)
    def __str__(self):
      return self.city

    def save_location(self):
        self.save()

    @classmethod
    def del_location(cls,id):
        cls.objects.get(id).delete() 
