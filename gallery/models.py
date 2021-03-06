from django.db import models


# Create your models here.

class Location(models.Model):
    photo_location = models.CharField(max_length=50)
    def __str__(self):
        return self.photo_location

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
    
    def update_location(self, update):
        self.photo_location = update 
        self.save()

    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate
     
          
class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self): 
        return self.category
     
    def save_category(self):   
        self.save()
          
    def delete_category(self):
        self.delete()
        
    def update_category(self, update):
        self.category = update
        self.save()
    @classmethod
    def get_category_id(cls, id):
        images = Category.objects.get(pk = id)
        return images

class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    image_photo = models.ImageField(upload_to = 'images/')

    def save_image(self):
        self.save()
          
    @classmethod   
    def get_image(cls,id):
        try:
            image = Image.objects.get(id=id)
            return image
        except DoesNotExist:
            return Image.objects.get(id=1) 
    
    @classmethod
    def search_by_category(cls,search_term):
        category = Category.objects.get(category=search_term)
        images = cls.objects.filter(category=category)
        return images

    @classmethod
    def filter_by_location(cls,locate):
        images=Image.objects.filter(location__photo_location__icontains=locate)
        return images