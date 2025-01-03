from django.db import models

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='gallery_images/')
    place = models.CharField(default="lucknow", max_length=50)

    def __str__(self):
        return f"{self.name}   -   {self.date}  -  {self.image}"
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15) 
    area = models.CharField(max_length=100)
    date = models.DateField()
    marriageDate = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.date}"
    


class Review(models.Model):
    gmailId = models.CharField(max_length=50)
    gmailProfile = models.ImageField(upload_to='user_profiles')
    review = models.TextField(max_length=100)
    date = models.DateField()
    stars = models.FloatField(max_length=5)


    def __str__(self):
        return f"{self.gmailId} - {self.date}"
