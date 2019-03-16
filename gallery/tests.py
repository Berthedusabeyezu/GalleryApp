from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.



def setUp(self):
          self.cat=Category(category='sport')
          self.location=Location(photo_location='Rwanda')
          self.image=Image(image='jpg',name='CACO',description="has a good shape",location=self.location,category=self.cat)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))
        self.assertTrue(isinstance(self.location,Location))
        self.assertTrue(isinstance(self.cat,Category))

    def test_save_image(self):
        self.cat.save()
        self.location.save()
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.cat.save()
        self.location.save()
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

   
    def test_get_images_by_category(self):
        images=Image.get_category_images(cat=self.cat)
        imagess=Image.objects.filter(category=self.cat)
        self.assertQuerysetEqual(images,imagess)

    def test_filter_by_location(self):
        images=Image.get_location_images(loc=self.location.pk)
        imagess=Image.objects.filter(location=self.location)
        self.assertQuerysetEqual(images,imagess)

    def test_update_image(self):
        new_image=Image.update_name(1,'bebe')
        self.assertTrue(self.image.name != new_image)

    def test_save_location(self):
        self.location.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_save_category(self):
        self.cat.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)
        
    def test_delete_location(self):
    
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

    def test_delete_category(self):
    
        self.cat.delete_category()
        categories= Category.objects.all()
        self.assertTrue(len(categories) == 0)

    def test_update_location(self):
        new_location=Location.update_all(1,'bebe','nana','nan')
        self.assertTrue(self.location != new_location)

    def test_update_category(self):
        new_category=Category.update_name(1,'bebe')
        self.assertTrue(self.cat.category != new_category)