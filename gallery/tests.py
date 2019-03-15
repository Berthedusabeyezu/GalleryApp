from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.


class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image= Location(photo_name = 'photo', description ='Good photo', location ='profile',category='sorpt')
    
    #Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Location))

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Location))
    
     # Testing Save Method
    def test_save_method(self):
        self.photo.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
    
    def test_update_method(self):
        self.update_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class ImageTestClass(TestCase):

    def setUp(self):
        self.photo = Location(photo_location = 'Image')
        self.photo.save_location()
        
        # Creating a new category and saving it
        self.new_category = categories(name = 'testing')
        self.new_category.save()

        self.new_image= Image(title = 'Test Image',post = 'This is a random test Post',location = self.photo)
        self.new_image.save()

        self.new_image.categories.add(self.new_category)

    def tearDown(self):
        Location.objects.all().delete()
        category.objects.all().delete()
        Image.objects.all().delete()