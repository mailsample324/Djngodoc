from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10,  default="")
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    


   

class Picture(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
