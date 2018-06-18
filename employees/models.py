from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255)
    job_title= models.TextField(blank=True, max_length=255)
    experience = models.IntegerField()
    image = models.FileField(upload_to='images/')


    def __str__(self):
        return self.name
