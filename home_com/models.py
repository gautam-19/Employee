from django.db import models

# Create your models here.
class Contact (models.Model):
    name = models.CharField(max_length= 120)
    email = models.EmailField(max_length=120)
    ph = models.CharField(max_length=20)
    info = models.CharField(max_length= 500)
    date = models.DateTimeField()

    #show entity with name
    def __str__(self):
        return self.name
