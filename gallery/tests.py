from django.test import TestCase
from .models import Image,Location,Category
import datetime as dt
import pyperclip
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



class CategoryTestClass(TestCase):

  # Set up method
  def setUp(self):
      self.travel= Category(name = 'Travel')


  # Testing  instance
  def test_instance(self):
      self.assertTrue(isinstance(self.travel,Category))    


  # Testing Save Method
  def test_save_method(self):
      self.travel.save_category()
      categories = Category.objects.all()
      self.assertTrue(len(categories) > 0)



  # Testing Delete Method
  def test_delete_method(self):
      self.food=Category(name='Food')
      self.food.save_category()
      self.travel.save_category()
      Category.del_category(self.food.id)
      categories = Category.objects.all()
      self.assertTrue(len(categories) == 1)              




class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new location and saving it
        self.nairobi= Location(city = 'Nairobi', country ='Kenya')
        self.nairobi.save_location()

        # Creating a new category and saving it
        self.new_category = Category(name = 'Travel')
        self.new_category.save_category()

        self.new_image= Image(image_name = 'Mt.Kenya',image_path='uploads/1517648653757.jpg' ,image_description = 'This is a random test Image',location = self.nairobi,category=self.new_category)
        self.new_image.save_image()

    # Tear Down method
    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()      

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))    

    # Testing Save Method
    def test_save_method(self):
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)  

    # Testing get all images Method
    def test_get_all_images_method(self):
        images = Image.get_all_images()
        self.assertTrue(len(images) > 0) 


    # Testing get all images Method
    def test_get_image_by_id_method(self):
        image = Image.get_image_by_id(self.new_image.id)
        self.assertEqual(image.id,self.new_image.id)          


    # Testing delete method
    def test_delete_image(self):
        Image.delete_image(self.new_image.id)
        images = Image.get_all_images()
        self.assertTrue(len(images) == 0)


    # Testing search image by category method
    def test_search_image(self):
        images=Image.search_image('Tra')
        imagess=Image.search_image('Taa')
        self.assertFalse(len(imagess) > 0)  
        self.assertTrue(len(images) > 0)  


    # Testing filter by location method
    def test_filter_by_location(self):
        images=Image.filter_by_location(self.nairobi.id)
        self.assertTrue(len(images) > 0)


    # Testing copy image url method
    def test_copy_image_url(self):            
      
        Image.copy_image_url(self.new_image.id)

        self.assertEqual(self.new_image.image_path.url,pyperclip.paste())       
