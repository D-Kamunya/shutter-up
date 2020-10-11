from django.test import TestCase
from .models import Image,Location,Category
import datetime as dt
# Create your tests here.
class LocationTestClass(TestCase):

  # Set up method
  def setUp(self):
      self.nairobi= Location(city = 'Nairobi', country ='Kenya')


  # Testing  instance
  def test_instance(self):
      self.assertTrue(isinstance(self.nairobi,Location))    


  # Testing Save Method
  def test_save_method(self):
      self.nairobi.save_location()
      locations = Location.objects.all()
      self.assertTrue(len(locations) > 0)



  # Testing Delete Method
  def test_delete_method(self):
      self.mbs=Location(city='Mombasa',country='Kenya')
      self.mbs.save_location()
      self.nairobi.save_location()
      Location.del_location(self.mbs.id)
      locations = Location.objects.all()
      self.assertTrue(len(locations) == 1)        

